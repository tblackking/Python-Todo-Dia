import pyzipper
from tqdm import tqdm
import sys

def crack_zip(passwords_list, zip_file_path):
    with pyzipper.AESZipFile(zip_file_path) as zip_file:
        with tqdm(passwords_list, "Cracking ZIP file") as pbar:
            for passwd in pbar:
                try:
                    zip_file.extractall(pwd=passwd.encode())
                    pbar.clear()
                    print("[!] PASSWORD:", passwd)
                    return
                except (RuntimeError, pyzipper.BadZipFile, pyzipper.LargeZipFile):
                    continue

if __name__ == "__main__":
    zip_file_path = sys.argv[1]
    wordlist_path = sys.argv[2]

    passwords = [line.strip() for line in open(wordlist_path, "r")]

    crack_zip(passwords_list=passwords, zip_file_path=zip_file_path)

    print("[!] Password not found, try another wordlist.")
