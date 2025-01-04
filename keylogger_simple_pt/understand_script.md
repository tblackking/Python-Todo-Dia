# README - Keylogger Script

## Introdução

Este script de keylogger tem como objetivo registrar todas as teclas pressionadas em um computador em um arquivo de log. Ele monitora eventos de teclado e grava a entrada em tempo real, registrando até que a tecla "ESC" seja pressionada, encerrando o monitoramento.

## Objetivo

O objetivo principal deste script é capturar as teclas pressionadas e armazená-las em um arquivo de log (`keyslogger.log`). Esse tipo de ferramenta pode ser útil em situações de diagnóstico, testes ou, com o devido propósito, em ambientes controlados e permitidos.

## Como Funciona

1. **Leitura de Eventos de Teclado**  
   O script utiliza a biblioteca `keyboard` para capturar eventos de teclado em tempo real. Ele monitora eventos `KEY_DOWN`, registrando cada tecla pressionada.

2. **Gravação Contínua**  
   A cada tecla pressionada, o script adiciona o caractere à `buffer` (linha temporária de armazenamento). Se a tecla pressionada for "esc", o script encerra a execução.

3. **Limitações e Raciocínio do Buffer**  
   - **MAX_DELAY**: Após um período de inatividade (definido em segundos, `MAX_DELAY`), o script força a gravação da buffer para evitar que teclas não digitadas se acumulem indefinidamente.  
   - **MAX_LINE_LENGTH**: Limita o tamanho de cada linha no arquivo de log. Quando o limite é atingido, o conteúdo da buffer é registrado e a buffer é limpa para começar novamente.

4. **Caracteres Comuns e suas Mapeações**  
   - `char == "space"`: Substitui espaços por um caractere espaço.  
   - `char == "enter"`: Substitui a tecla "Enter" por uma quebra de linha (`\n`).  
   - `char == "backspace"`: Remove o último caractere da buffer, se houver.

5. **Especificidade da Arquivação**  
   - Após cada gravação, se a buffer for maior que o limite de caracteres, ela é truncada.  
   - A gravação contínua evita acúmulo de dados desnecessários, mantendo o desempenho otimizado.

6. **Encerramento do Script**  
   - O script monitora constantemente até que a tecla "esc" seja pressionada. Isso interrompe o processo e escreve a buffer final para o arquivo antes de finalizar.

## Estrutura do Código

### Variáveis Globais

- **`OUTPUT_FILE`**: Nome do arquivo onde as teclas digitadas serão registradas (`keyslogger.log`).  
- **`MAX_LINE_LENGTH`**: Tamanho máximo das linhas no arquivo de log.  
- **`MAX_DELAY`**: Tempo máximo em segundos sem entrada de teclado antes de forçar a gravação.

### Função `write_to_file(buffer)`

- **Descrição**: Grava o conteúdo da buffer no arquivo de log especificado.  
- **Uso**: É chamada periodicamente para armazenar os caracteres digitados, respeitando os limites de tempo e tamanho.

### Função `keylogger_exec()`

- **Descrição**: Responsável por monitorar e processar os eventos do teclado.  
- **Logica Complexa**:  
  - A lógica de gravação considera tanto o tempo (`MAX_DELAY`) como o tamanho da buffer (`MAX_LINE_LENGTH`).  
  - Processa diferentes tipos de eventos de teclado, tratando de forma específica teclas como `space`, `enter`, e `backspace`.  
  - Quando a buffer excede o limite de caracteres ou o tempo de inatividade, escreve no arquivo.  
  - Continua capturando teclas até que a tecla "esc" seja pressionada para parar o loop.

### `if __name__ == "__main__":`

- **Descrição**: Serve como ponto de entrada principal do script. Chama a função `keylogger_exec()` para iniciar o monitoramento.

---

## Exemplo de Execução

1. Certifique-se de instalar a biblioteca `keyboard`:
   ```bash
   pip install keyboard


Considerações de Segurança
Propósito: Este script deve ser usado com responsabilidade e em conformidade com as políticas legais e éticas locais. O uso indevido pode infringir a privacidade das pessoas e comprometer a segurança.
Autorização: Certifique-se de ter a devida permissão para utilizar este script em ambientes de trabalho ou dispositivos.
Privacidade: Evite o uso em computadores sem consentimento, pois isso pode violar a privacidade das pessoas.
