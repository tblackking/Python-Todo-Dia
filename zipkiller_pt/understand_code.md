# Script de Quebra de Senha de Arquivos ZIP

Este script utiliza as bibliotecas `pyzipper` e `tqdm` para realizar ataques de força bruta em arquivos ZIP protegidos por senha. Ele itera sobre uma lista de senhas (wordlist) tentando desbloquear o arquivo. O objetivo é identificar a senha correta que permite extrair o conteúdo do arquivo ZIP.

---

## 📋 Visão Geral do Script

### 🚀 Funcionamento
O script segue as etapas principais:
1. **Leitura do Caminho do Arquivo ZIP e da Wordlist**:
   - Os caminhos do arquivo ZIP e da wordlist são passados como argumentos ao script na linha de comando.
2. **Leitura das Senhas da Wordlist**:
   - As senhas do arquivo da wordlist são carregadas em uma lista.
3. **Ataque de Força Bruta**:
   - Utilizando a biblioteca `pyzipper`, o script tenta extrair o conteúdo do arquivo ZIP usando cada senha da lista.
   - A biblioteca `tqdm` fornece uma barra de progresso para acompanhar o andamento do ataque.
4. **Resultado**:
   - Caso uma senha válida seja encontrada, ela é exibida no terminal.
   - Caso contrário, o script termina sem sucesso.

---

## 📂 Estrutura do Código

### 🔧 Função: `crack_zip(passwords_list, zip_file_path)`
Essa é a função principal do script. Ela realiza o processo de força bruta no arquivo ZIP.

- **Parâmetros**:
  - `passwords_list` (list): Uma lista contendo as senhas que serão testadas.
  - `zip_file_path` (str): O caminho do arquivo ZIP que será analisado.

- **Fluxo da Função**:
  1. **Abre o Arquivo ZIP**:
     Utiliza o `pyzipper.AESZipFile` para abrir o arquivo ZIP no modo de leitura.
  2. **Iteração sobre a Wordlist**:
     A barra de progresso `tqdm` é usada para iterar sobre a lista de senhas. Para cada senha:
     - O script tenta extrair o conteúdo do ZIP com a senha atual.
     - Caso a senha esteja correta, o processo é interrompido e a senha é exibida.
     - Se a senha falhar, ocorre um tratamento de exceções para ignorar erros e continuar.
  3. **Exibe a Senha Encontrada**:
     Quando a senha correta é identificada, ela é exibida no terminal com a mensagem `[!] PASSWORD: <senha>`.

### 🔧 Bloco Principal: `if __name__ == "__main__":`
Este é o ponto de entrada do script, onde as entradas do usuário são tratadas e a função principal é chamada.

- **Parâmetros Recebidos**:
  - `sys.argv[1]`: Caminho do arquivo ZIP.
  - `sys.argv[2]`: Caminho da wordlist.

- **Etapas**:
  1. **Carrega a Wordlist**:
     Lê as senhas do arquivo especificado em `sys.argv[2]`, removendo quebras de linha.
  2. **Chama a Função `crack_zip`**:
     Passa a lista de senhas e o caminho do arquivo ZIP para a função de quebra.
  3. **Finaliza**:
     Caso nenhuma senha seja encontrada, uma mensagem será exibida no terminal.

---

## 📚 Bibliotecas Utilizadas

### 1. `pyzipper`
- Biblioteca para manipulação de arquivos ZIP com suporte a criptografia AES.
- Permite abrir, ler, escrever e extrair arquivos ZIP protegidos por senha.
- Site: [pyzipper](https://pypi.org/project/pyzipper/)

### 2. `tqdm`
- Fornece barras de progresso personalizáveis.
- Usada para exibir o progresso durante o ataque de força bruta.
- Site: [tqdm](https://tqdm.github.io/)

### 3. `sys`
- Biblioteca padrão do Python usada para capturar os argumentos da linha de comando.

---

## ⚙️ Como Utilizar o Script

1. **Pré-requisitos**:
   - Python 3.6 ou superior.
   - Instale as bibliotecas necessárias:
     ```bash
     pip install pyzipper tqdm
     ```

2. **Prepare a Wordlist**:
   - Crie ou baixe um arquivo `.txt` contendo uma lista de senhas, uma por linha.

3. **Execute o Script**:
   - Use o terminal para executar o script. A sintaxe é:
     ```bash
     python script.py <caminho_do_arquivo_zip> <caminho_da_wordlist>
     ```

   - Exemplo:
     ```bash
     python script.py arquivo.zip senhas.txt
     ```

4. **Resultado**:
   - Se uma senha válida for encontrada, ela será exibida no terminal:
     ```
     [!] PASSWORD: minha_senha
     ```

---

## ⚠️ Observações

- **Responsabilidade**: Este script é apenas para fins educacionais. Certifique-se de usá-lo apenas em arquivos para os quais você possui permissão legal.
- **Limitações**:
  - Apenas arquivos ZIP com criptografia compatível com `pyzipper` podem ser processados.
  - O desempenho depende do tamanho da wordlist e da complexidade da senha.

---

## 🛠️ Possíveis Melhorias

- Adicionar suporte para multithreading ou multiprocessing para aumentar a velocidade.
- Implementar um limite para o número de tentativas em arquivos ZIP grandes.
- Criar uma interface gráfica para facilitar o uso.

---

## 📞 Suporte
Caso tenha dúvidas ou precise de suporte, sinta-se à vontade para entrar em contato.

---
