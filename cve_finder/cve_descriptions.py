import nvdlib

KEY = "YOUR KEY"


def _display_cve(cve):
            """
            Exibe as informações de uma CVE de forma estruturada.

            :param cve: Objeto CVE retornado pela biblioteca nvdlib.
            """
            id_cve = f"[!] ID: {cve.id}"
            description = f"[!] Description: {cve.descriptions[0].value}"
            date_publ = f"[!] Data de publication: {cve.published}"
            last_update = f"[!] Last modification: {cve.lastModified}"
            link = f"[!] Link: https://nvd.nist.gov/vuln/detail/{cve.id}"
            if hasattr(cve, 'v31score'):
               score_cvss31 =  f"[!][!] Score CVSS v3.1: {cve.v31score} ({cve.v31severity})"
            else: 
               score_cvss31 = ''
            
            if hasattr(cve, 'v30score'):
                score_cvss30 = f"[!][!] Score CVSS v3.0: {cve.v30score} ({cve.v30severity})"
            else:
                score_cvss30 = ''
            
            if hasattr(cve, 'v2score'):
                score_cv2score = f"[!][!] Score CVSS v2: {cve.v2score} ({cve.v2severity})"
            else:
                score_cv2score = ''
            
            return id_cve, description, date_publ, last_update, link, score_cvss31, score_cvss30, score_cv2score


cve_list = open('CVEs_not_duplicated_25_04_2025.txt').read().splitlines()


for cve in cve_list:
    results = nvdlib.searchCVE(cveId=cve, key=KEY)[0]

    id_cve_, description_, date_publ_, last_update_, link_, score_cvss31_, score_cvss30_, score_cv2score_ = _display_cve(results)
    
    build_infos = f'{description_}|{date_publ_}|{last_update_}|{link_}|{score_cvss31_}|{score_cvss30_}|{score_cv2score_}'
    
    print(build_infos)

    with open('CVE_INFOS_25_04_2025.txt', 'a', encoding='utf-8') as file:
         file.write(f'{id_cve_}|{build_infos}' + '\n')