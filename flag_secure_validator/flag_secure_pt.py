import os
import zipfile
import re
import xml.etree.ElementTree as ET

# === CONFIGURAÇÃO ===
APK_PATH = "app_01.apk"  # Caminho do APK a ser analisado
EXTRACT_PATH = "apk_extracted"

# === FUNÇÃO PARA EXTRAIR O APK ===
def extract_apk(apk_path, extract_path):
    if not os.path.exists(extract_path):
        os.makedirs(extract_path)
    with zipfile.ZipFile(apk_path, 'r') as apk:
        apk.extractall(extract_path)
    print(f"[+] APK extraído em: {extract_path}")

# === FUNÇÃO PARA ANALISAR REFERÊNCIAS FLAG_SECURE NOS .DEX ===
def search_flag_secure_in_dex(extract_path):
    dex_files = [f for f in os.listdir(extract_path) if f.endswith(".dex")]
    results = []
    for dex in dex_files:
        with open(os.path.join(extract_path, dex), "rb") as f:
            content = f.read()
            matches = re.findall(b"FLAG_SECURE", content)
            if matches:
                results.append((dex, len(matches)))
    return results

# === FUNÇÃO PARA ANALISAR O ANDROIDMANIFEST.XML ===
def analyze_manifest(extract_path):
    manifest_path = os.path.join(extract_path, "AndroidManifest.xml")
    try:
        # Parse básico (o Manifest vem binário no APKTool, mas em alguns APKs já está legível)
        tree = ET.parse(manifest_path)
        root = tree.getroot()
        activities = []
        for elem in root.iter():
            if 'activity' in elem.tag:
                activities.append(elem.attrib)
        return activities
    except Exception as e:
        return f"[!] Não foi possível analisar o Manifest diretamente: {e}"

# === EXECUÇÃO ===
if __name__ == "__main__":
    if not os.path.exists(APK_PATH):
        print(f"[ERRO] APK não encontrado em {APK_PATH}")
        exit(1)

    extract_apk(APK_PATH, EXTRACT_PATH)

    print("\n[1] Analisando referências a FLAG_SECURE nos arquivos DEX...")
    flag_results = search_flag_secure_in_dex(EXTRACT_PATH)
    if flag_results:
        for dex, count in flag_results:
            print(f"    - Encontrado {count} referência(s) em {dex}")
    else:
        print("    [-] Nenhuma referência a FLAG_SECURE encontrada nos DEX.")

    print("\n[2] Analisando AndroidManifest.xml...")
    manifest_activities = analyze_manifest(EXTRACT_PATH)
    if isinstance(manifest_activities, list):
        print(f"    [+] {len(manifest_activities)} atividades encontradas no Manifest.")
        for act in manifest_activities:
            print(f"    - {act}")
    else:
        print(manifest_activities)

    print("\n[✅] Análise concluída!")
