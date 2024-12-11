import whois 

def domain_is_true(domain):
    whois_ = whois.whois(domain)
    
    if bool(whois_.domain_name): 
        return whois_
    else:
        return False 
    

def informations_about_domain(domain_name):
    w = domain_is_true(domain=domain_name)
    if w:
        print(f'\n=============================={domain_name}==============================')
        print('DOMAIN REGISTER: ', w.registrar)
        print('WHOIS SERVER: ', w.whois_server)
        print('DOMAIN CREATION DATE: ', w.creation_date)
        print('EXPIRATION DATE: ', w.expiration_date)
        print(w)
        print(f'=============================={domain_name}==============================\n')
        

if __name__ == "__main__":

    host = input('[$] HOST: ')

    print("\n[!] Executindo whois validator [!]\n[!!] If anything data return, please consult again [!!]\n")

    informations_about_domain(domain_name=host)