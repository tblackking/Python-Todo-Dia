import hashlib
import argparse
from colorama import init, Fore


def haskiller_mb_pt(hash_value, wordlist_path, hash_type, positive_c, negative_c, reset_c):
    try:
        
        hash_algorithms = {
            'md5': hashlib.md5,
            'sha1': hashlib.sha1,
            'sha224': hashlib.sha224,
            'sha256': hashlib.sha256,
            'sha384': hashlib.sha384,
            'sha512': hashlib.sha512,
            'blake2b': hashlib.blake2b,
            'blake2s': hashlib.blake2s,
        }

        algorthm_name = hash_type.lower()
        if algorthm_name not in hash_algorithms:
            raise ValueError(f"[//] Algorithm {algorthm_name} not supported")

    
        with open(fr'{wordlist_path}', 'r') as file:
            hash_function = hash_algorithms[algorthm_name]

            
            for line in file:
                word = line.strip()
                hash_done = hash_function(word.encode()).hexdigest()

               
                print(f"{reset_c}[TRY] {hash_value} X {hash_done}/{word}   {reset_c}")

                
                if hash_done == hash_value:
                    print(f"\n{positive_c}[FIND] {hash_value}/{word} X {hash_done}/{word}    {reset_c}\n")
                    return  #
            print(f"{negative_c}[NOT FOUND] Hash não encontrado na wordlist.{reset_c}")

    except Exception as error:
        print(f"{negative_c}\n[ERROR] - {error}     {reset_c}\n")


if __name__ == "__main__":
    init()
    GREEN_COLOR = Fore.GREEN
    RESET_COLOR = Fore.RESET
    RED_COLOR = Fore.RED

 
    parser = argparse.ArgumentParser(description="Hash Killer Script")
    parser.add_argument("--hash", required=True, help="The target hash to crack")
    parser.add_argument("--wordlist", required=True, help="Path to the wordlist file")
    parser.add_argument("--type", required=True, help="Type of the hash (e.g., md5, sha256)")

    args = parser.parse_args()

   
    haskiller_mb_pt(
        hash_value=args.hash,
        wordlist_path=args.wordlist,
        hash_type=args.type,
        positive_c=GREEN_COLOR,
        negative_c=RED_COLOR,
        reset_c=RESET_COLOR,
    )
