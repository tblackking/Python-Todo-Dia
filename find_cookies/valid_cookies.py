from playwright.sync_api import sync_playwright

urls = open(r"find_cookies\urls_to_verify.txt", "r", encoding="utf-8").read().splitlines()

with sync_playwright() as p:
    browser = p.firefox.launch(headless=True)
    context = browser.new_context(
    user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0 Safari/537.36",
    viewport={"width": 1280, "height": 720},
    java_script_enabled=True,
    locale="pt-BR")
    for url in urls:
        try:
            page = browser.new_page()
            page.goto(f"https://{url}")
            content = page.content()

            # Verifica se existe alguma palavra-chave comum nos banners
            if any(kw in content.lower() for kw in ['cookie', 'consent', 'aceita os cookies']):
                print(f"[✔] Tarja de cookies detectada em: {url}")
                with open("contem_tarja_cookies.txt", "a", encoding="utf-8") as file:
                    file.write(url + "\n")
            else:
                print(f"[✘] Sem tarja de cookies detectada em: {url}")
        except Exception as error:
            print(f"[✘] {url} not response")
            pass

    browser.close()

