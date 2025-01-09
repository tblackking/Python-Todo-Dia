# Sistema de Transferência de Arquivos via Socket

Este repositório contém dois scripts para transferência de arquivos utilizando sockets em Python. Os scripts são:

1. **Cliente (`client.py`)**: Envia arquivos para um servidor.
2. **Servidor (`server.py`)**: Recebe e armazena arquivos enviados pelo cliente.

---

## 📋 Funcionamento

### 1. **`client.py`**
O script do cliente permite ao usuário enviar arquivos para o servidor. 

#### **Detalhamento do Código**

##### Variáveis Principais:
- **`HOST`**: Endereço IP do servidor ao qual o cliente se conecta. Por padrão, `127.0.0.1` (localhost).
- **`PORT`**: Porta utilizada para a conexão. Padrão: `5000`.
- **`BUFFER_SIZE`**: Tamanho do buffer para transmissão de dados. Padrão: `4096` bytes.
- **`MAX_FILE_SIZE`**: Tamanho máximo permitido para envio de arquivos (100 MB).

##### **Funções**
- **`send_file(client_socket, filename)`**: 
  - Envia um arquivo para o servidor.
  - Verifica se o arquivo existe e se o tamanho é permitido.
  - Envia o nome e o tamanho do arquivo ao servidor, seguido pelo conteúdo do arquivo em blocos de tamanho `BUFFER_SIZE`.
  - **Exemplo de Uso:** 
    ```python
    send_file(client_socket, 'meuarquivo.txt')
    ```

##### **Fluxo Principal**
1. Conecta ao servidor utilizando `socket.socket`.
2. Solicita ao usuário o caminho do arquivo a ser enviado ou o comando `sair` para encerrar.
3. Verifica se o caminho do arquivo é válido. Caso seja, chama `send_file`.
4. Envia o comando `EXIT` para encerrar a conexão.

---

### 2. **`server.py`**
O script do servidor recebe os arquivos enviados pelo cliente e os armazena em um diretório específico.

#### **Detalhamento do Código**

##### Variáveis Principais:
- **`HOST`**: Endereço IP onde o servidor escutará conexões. Padrão: `0.0.0.0` (todas as interfaces).
- **`PORT`**: Porta utilizada para a conexão. Padrão: `5000`.
- **`BUFFER_SIZE`**: Tamanho do buffer para transmissão de dados. Padrão: `4096` bytes.
- **`SAVE_DIR`**: Diretório onde os arquivos recebidos serão armazenados. Padrão: `recebidos/`.

##### **Fluxo Principal**
1. Cria o diretório `SAVE_DIR` caso não exista.
2. Configura o servidor para escutar conexões com `socket.socket`.
3. Aceita a conexão de um cliente e exibe o endereço do cliente conectado.
4. Aguarda mensagens do cliente:
   - Recebe o nome do arquivo e confirma recebimento.
   - Recebe o tamanho do arquivo e confirma recebimento.
   - Lê o conteúdo do arquivo em blocos de tamanho `BUFFER_SIZE` e salva no diretório especificado.
   - Encerra a conexão ao receber o comando `EXIT`.

---

## 📂 Estrutura de Arquivos

```plaintext
.
├── client.py       # Script do cliente para envio de arquivos
├── server.py       # Script do servidor para recepção de arquivos
└── recebidos/      # Diretório para armazenar arquivos recebidos (criado automaticamente pelo servidor)
```

---

## 🛠️ Como Usar

### Passo 1: Configurar o Servidor
1. Certifique-se de que o Python 3 está instalado.
2. Execute o script do servidor:
   ```bash
   python server.py
   ```
3. O servidor estará aguardando conexões na porta `5000`.

### Passo 2: Enviar Arquivos com o Cliente
1. Certifique-se de que o Python 3 está instalado.
2. Execute o script do cliente:
   ```bash
   python client.py
   ```
3. Insira o caminho do arquivo a ser enviado ou digite `sair` para encerrar a conexão.

---

## ⚙️ Requisitos

- Python 3.6 ou superior.
- Conexão em rede entre o cliente e o servidor (podem ser executados na mesma máquina para testes).

---

## 📌 Observações

- Certifique-se de que os arquivos enviados não ultrapassem o tamanho máximo de 100 MB (ajustável na variável `MAX_FILE_SIZE` no cliente).
- Verifique se a porta `5000` está disponível e não bloqueada pelo firewall.
- O script do servidor cria automaticamente o diretório `recebidos/` caso ele não exista.

---