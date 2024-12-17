import dns
import dns.resolver 
import argparse


from display_tool import DEFAULT_LINK, BYBLACK, ASCII_PYTHON_TODO_DIA

def get_dns_info(target, specifydns='', listypes=["A", "AAAA", "CNAME", "MX", "NS", "SOA", "TXT"]):
    resolver = dns.resolver.Resolver()
    
    if specifydns !=  '':
        try: 
            answers = resolver.resolve(target, specifydns)
            print(f'\nDNS RECORDS FOR {target} | [{specifydns}]\n')
            for iten in answers: 
                print(f'> {iten}')
        except dns.resolver.NoAnswer: 
            pass 
    else:
        for type in listypes: 
            try:
                answers = resolver.resolve(target, type)
                print(f'\nDNS RECORDS FOR {target} | [{type}]')
                for iten in answers: 
                    print(f'> {iten}')
            except dns.resolver.NoAnswer:
                continue

if __name__ == "__main__":

    print(ASCII_PYTHON_TODO_DIA)
    print(DEFAULT_LINK)
    
    parser_ = argparse.ArgumentParser()
    parser_.add_argument("host", help='')
    parser_.add_argument("-spf", "--specify", help='', default='')
    
    args = parser_.parse_args()
    host = args.host
    specify = args.specify 
    
    get_dns_info(target=host, specifydns=specify)
    