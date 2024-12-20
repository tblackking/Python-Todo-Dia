import string
import random
import argparse


def generate_password(alp_caps=True, alp_lower=True, numbs=True, simbs=True, quant_carac=25):
   
    options = (
        (string.ascii_uppercase if alp_caps else '') +
        (string.ascii_lowercase if alp_lower else '') +
        ('123456789' if numbs else '') +
        ('[]{}()*;/,_-!@' if simbs else '')
    )
    
 
    if not options:
        raise ValueError("Pelo menos uma categoria de caracteres deve ser ativada!")
    
    return ''.join(random.choices(options, k=quant_carac))


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Gerador de senhas personalizável")
    parser.add_argument("-u", "--uppercase", action="store_true", help="Incluir letras maiúsculas")
    parser.add_argument("-l", "--lowercase", action="store_true", help="Incluir letras minúsculas")
    parser.add_argument("-n", "--numbers", action="store_true", help="Incluir números")
    parser.add_argument("-s", "--symbols", action="store_true", help="Incluir símbolos")
    parser.add_argument("-c", "--characters", type=int, default=25, help="Quantidade de caracteres na senha (padrão: 25)")
    
    args = parser.parse_args()
   
    try: 
        password = generate_password(
        alp_caps=args.uppercase,
        alp_lower=args.lowercase,
        numbs=args.numbers,
        simbs=args.symbols,
        quant_carac=args.characters)

        print(f"{password}")
    except ValueError as e:
       print("Erro: Você deve habilitar pelo menos uma categoria de caracteres (use -u, -l, -n ou -s).")
