import pikepdf
from tqdm import tqdm
import sys


def kill_pdf(passwords_list, pdf_file):
    with tqdm(passwords_list, "Killyng PDF locked") as pbar:
        for passwd in pbar:
            try:
                with pikepdf.open(pdf_file, password=passwd) as pdf:
                    pbar.clear()
                    print("[!] PASSWORD:", passwd)
                    return  
            except pikepdf.PasswordError:
                continue


if __name__ == "__main__":
    pdf_file = sys.argv[1]

    wordlist = sys.argv[2]

    passwords = [ line.strip() for line in open(wordlist) ]

    kill_pdf(passwords_list=passwords, pdf_file=pdf_file)

