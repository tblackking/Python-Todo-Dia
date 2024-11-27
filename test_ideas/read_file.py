LIST_SUB = input("LIST_SUB: ")



list_to_read = open(fr"{LIST_SUB}", 'r', encoding='utf-8').read().splitlines()
print(list_to_read)