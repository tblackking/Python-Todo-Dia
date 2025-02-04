
# Detalhamento Técnico do Script

Este script tem o objetivo de extrair e exibir metadados de arquivos de imagem (JPG, PNG, BMP, GIF, TIFF) e PDF. Ele utiliza a biblioteca `PIL` (Python Imaging Library) para imagens e a biblioteca `pikepdf` para PDFs. Além disso, o script pode ser executado a partir da linha de comando, recebendo o caminho de um arquivo como argumento.

## Dependências

- **sys**: Biblioteca padrão para manipulação de parâmetros de linha de comando e funções do sistema.
- **pprint**: Biblioteca padrão para imprimir objetos de forma mais legível (por exemplo, dicionários).
- **PIL** (Python Imaging Library, também conhecida como Pillow): Biblioteca para abrir, manipular e salvar arquivos de imagem.
- **pikepdf**: Biblioteca para manipulação de arquivos PDF.

## Funções

### 1. `get_image_metadata(image_file)`
Essa função tem como objetivo extrair metadados de uma imagem fornecida como argumento.

#### Passos da função:

1. **Abrir a imagem**:
   - `image = Image.open(image_file)`: Abre a imagem no caminho especificado.
   
2. **Criar dicionário com informações básicas da imagem**:
   - `info_dict = { ... }`: A função cria um dicionário com os seguintes dados básicos:
     - `Filename`: Nome do arquivo.
     - `Image Size`: Tupla com a altura e largura da imagem.
     - `Image Height`/`Image Width`: Altura e largura da imagem.
     - `Image Format`: Formato da imagem (JPG, PNG, etc.).
     - `Image Mode`: Modo de cor da imagem (RGB, L, etc.).
     - `Image is Animated`: Se a imagem é animada (ex.: GIFs).
     - `Frames in Image`: Número de quadros na animação (se for uma imagem animada).
   
3. **Obter metadados EXIF**:
   - `exifdata = image.getexif()`: Obtém os dados EXIF da imagem, que são metadados armazenados na própria imagem.
   - O script percorre cada tag de EXIF e adiciona ao dicionário `info_dict`.
   - **Conversão de dados EXIF**:
     - Se o valor de uma tag EXIF for um objeto `bytes`, ele é decodificado para uma string com `data.decode()`.
   
4. **Retorno**:
   - `return info_dict`: Retorna o dicionário `info_dict` com todos os metadados extraídos.

### 2. `get_pdf_metadata(pdf_file)`
Essa função tem como objetivo extrair metadados de um arquivo PDF fornecido como argumento.

#### Passos da função:

1. **Abrir o PDF**:
   - `pdf = pikepdf.Pdf.open(pdf_file)`: Abre o arquivo PDF especificado utilizando a biblioteca `pikepdf`.

2. **Retornar metadados**:
   - `return dict(pdf.docinfo)`: A função retorna os metadados do PDF como um dicionário, onde as chaves são os nomes dos metadados (como autor, título, etc.), e os valores são os respectivos valores desses metadados.

3. **Tratamento de exceções**:
   - Se houver um erro ao tentar abrir o PDF ou extrair seus metadados, ele captura a exceção e imprime a mensagem de erro:
   - `except Exception as e: print(f"Erro ao extrair metadados do PDF: {e}")`.

4. **Retorno**:
   - Caso haja erro ao abrir ou ler o PDF, um dicionário vazio é retornado `{}`.

### 3. Bloco `if __name__ == "__main__":`
Este bloco garante que o script seja executado apenas quando for chamado diretamente da linha de comando.

#### Passos da execução:

1. **Obter o arquivo a partir dos argumentos**:
   - `file = sys.argv[1]`: O caminho do arquivo é passado como argumento na linha de comando. O script pega o primeiro argumento (`sys.argv[1]`), que é o arquivo a ser analisado.

2. **Verificar a extensão do arquivo**:
   - `if file.endswith(".pdf")`: Se o arquivo for um PDF (baseado na extensão `.pdf`), a função `get_pdf_metadata` é chamada e os metadados são exibidos.
   - `elif file.lower().endswith((".jpg", ".jpeg", ".png", ".bmp", ".gif", ".tiff"))`: Se o arquivo for uma imagem (uma das extensões especificadas), a função `get_image_metadata` é chamada e os metadados são exibidos.
   
3. **Formato de arquivo não suportado**:
   - `else: print(f"Unsupported file format: {file}")`: Se o arquivo não for nem um PDF nem uma imagem, é exibida uma mensagem informando que o formato não é suportado.

## Execução

1. O script é executado a partir da linha de comando passando o caminho de um arquivo:
   ```bash
   python script.py caminho/para/arquivo.pdf
   ```
   
2. Dependendo do tipo de arquivo (imagem ou PDF), ele irá chamar a função apropriada e exibir os metadados ou uma mensagem de erro caso o formato seja desconhecido.

## Exemplo de Saída

- Para um **PDF**, o retorno pode ser algo assim:
  ```json
  {'/Title': 'Example PDF',
   '/Author': 'John Doe',
   '/Creator': 'Python Script',
   '/Producer': 'pikepdf 1.18.1'}
  ```

- Para uma **imagem**, a saída pode ser:
  ```json
  {
    'Filename': 'example.jpg',
    'Image Size': (1920, 1080),
    'Image Height': 1080,
    'Image Width': 1920,
    'Image Format': 'JPEG',
    'Image Mode': 'RGB',
    'Image is Animated': False,
    'Frames in Image': 1,
    'Make': 'Canon',
    'Model': 'EOS 5D Mark III',
    ...
  }
  ```

## Conclusão

Este script é útil para obter informações sobre arquivos PDF e imagens de maneira simples e rápida. Ele pode ser ampliado para outros tipos de arquivos ou ajustado para capturar metadados adicionais conforme necessário.
