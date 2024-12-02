import requests 


def xframe_valid_mb_pt(url):
    try:
        response = requests.head(url, allow_redirects=True)

        headers_resp = response.headers

        if "X-Frame-Options" in headers_resp:
            return True 
        else: 
            return False 
        
    except requests.RequestException as e:
        return f"[ERROR] - {e}"





print(xframe_valid_mb_pt('https://google.com.br'))