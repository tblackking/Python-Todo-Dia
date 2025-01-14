# Documentação do Script Hash Killer

## Introdução

Este script foi projetado para ajudar os usuários a "quebrar" ou encontrar o texto original de um determinado hash, comparando-o com entradas em uma wordlist. O script suporta vários tipos de hash, como MD5, SHA1, SHA256, entre outros. Abaixo está uma explicação detalhada de cada parte do script para ajudar você a entender sua funcionalidade e propósito.

---

## Explicação do Script

### **Importação de Bibliotecas**

```python
import hashlib
import argparse
from colorama import init, Fore
```

- `hashlib`: Fornece acesso a vários algoritmos de hash e digest de mensagem.
- `argparse`: Ajuda a interpretar argumentos passados pela linha de comando.
- `colorama`: Habilita saída de texto colorido no terminal para um feedback visual melhor.

### **Função: `haskiller_mb_pt`**

Esta função executa a lógica de quebra de hash.

```python
def haskiller_mb_pt(hash_value, wordlist_path, hash_type, positive_c, negative_c, reset_c):
```

#### **Parâmetros:**
- `hash_value`: O hash que você deseja quebrar.
- `wordlist_path`: Caminho para o arquivo contendo os possíveis valores em texto simples.
- `hash_type`: O tipo de hash usado para gerar o valor fornecido (por exemplo, MD5, SHA256).
- `positive_c`, `negative_c`, `reset_c`: Códigos de cores para imprimir mensagens de sucesso, falha e texto padrão, respectivamente.

#### **Seleção do Algoritmo de Hash**

```python
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
```

Este dicionário mapeia os nomes dos algoritmos de hash para suas respectivas funções em `hashlib`. Isso garante flexibilidade e permite a fácil adição de novos tipos de hash suportados por `hashlib`.

#### **Validação do Algoritmo de Hash**

```python
    algorthm_name = hash_type.lower()
    if algorthm_name not in hash_algorithms:
        raise ValueError(f"[//] Algorithm {algorthm_name} not supported")
```

- Converte o tipo de hash para minúsculas e verifica se ele é suportado. Caso contrário, uma exceção `ValueError` é lançada.

#### **Leitura do Arquivo Wordlist**

```python
    with open(fr'{wordlist_path}', 'r') as file:
        hash_function = hash_algorithms[algorthm_name]
```

- Abre o arquivo da wordlist em modo de leitura e atribui a função de hash apropriada com base no tipo selecionado.

#### **Lógica de Comparação de Hash**

```python
        for line in file:
            word = line.strip()
            hash_done = hash_function(word.encode()).hexdigest()

            print(f"{reset_c}[TRY] {hash_value} X {hash_done}/{word}   {reset_c}")

            if hash_done == hash_value:
                print(f"\n{positive_c}[FIND] {hash_value}/{word} X {hash_done}/{word}    {reset_c}\n")
                return
```

- Itera sobre cada linha na wordlist.
- Remove espaços extras e codifica a palavra antes de calcular seu hash.
- Imprime cada tentativa de hash.
- Se uma correspondência for encontrada, imprime a mensagem de sucesso e sai da função.

#### **Tratamento de Erros**

```python
    except Exception as error:
        print(f"{negative_c}\n[ERROR] - {error}     {reset_c}\n")
```

- Captura quaisquer erros que ocorram durante a execução e imprime uma mensagem de erro.

---

### **Bloco Principal de Execução**

```python
if __name__ == "__main__":
    init()
    GREEN_COLOR = Fore.GREEN
    RESET_COLOR = Fore.RESET
    RED_COLOR = Fore.RED
```

- `init()`: Inicializa o `colorama` para habilitar a saída colorida.
- Define códigos de cores para sucesso, falha e texto padrão.

#### **Interpretação dos Argumentos**

```python
    parser = argparse.ArgumentParser(description="Hash Killer Script")
    parser.add_argument("--hash", required=True, help="The target hash to crack")
    parser.add_argument("--wordlist", required=True, help="Path to the wordlist file")
    parser.add_argument("--type", required=True, help="Type of the hash (e.g., md5, sha256)")

    args = parser.parse_args()
```

- Configura o script para aceitar argumentos da linha de comando para o hash alvo, o arquivo da wordlist e o tipo de hash.

#### **Chamada da Função**

```python
    haskiller_mb_pt(
        hash_value=args.hash,
        wordlist_path=args.wordlist,
        hash_type=args.type,
        positive_c=GREEN_COLOR,
        negative_c=RED_COLOR,
        reset_c=RESET_COLOR,
    )
```

- Passa os argumentos interpretados para a função `haskiller_mb_pt`.

---

## Instruções de Uso

### **Executando o Script**

Para executar o script, use o seguinte formato de comando:

```bash
python script_name.py --hash <hash_alvo> --wordlist <caminho_para_wordlist> --type <tipo_de_hash>
```

### **Exemplo**

```bash
python hashkiller.py --hash 5d41402abc4b2a76b9719d911017c592 --wordlist words.txt --type md5
```

---

## Notas e Dicas

1. **Qualidade da Wordlist**: Certifique-se de que a wordlist contenha palavras relevantes para aumentar as chances de encontrar o texto original.
2. **Precisão do Tipo de Hash**: Forneça o tipo de hash correto; caso contrário, o script não funcionará.
3. **Tratamento de Erros**: Se encontrar erros, verifique os caminhos dos arquivos e os tipos de hash.
4. **Considerações de Desempenho**: Wordlists grandes podem desacelerar o script; considere usar hardware mais rápido ou bibliotecas otimizadas se necessário.

---

## Conclusão

Este script demonstra um método básico, mas poderoso, para quebra de hashes usando Python. Ao aproveitar algoritmos de hash comuns e leitura eficiente de arquivos, ele serve como uma ferramenta prática para profissionais de segurança e entusiastas.
