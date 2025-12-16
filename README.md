# COIN REPORT 💸

Um projeto Python simples para monitorar o preço do Bitcoin em relação ao Real Brasileiro (BRL) usando a API CoinGecko e enviar um relatório por e-mail via Resend.

## Funcionalidades

* **Monitoramento de Preços:** Obtém o preço atual do Bitcoin e a variação percentual das últimas 24 horas.
* **Relatório Visual:** Gera um relatório de status em formato HTML (e-mail) indicando se o Bitcoin está em "alta" ou "queda".
* **Notificação por E-mail:** Envia o relatório diário para um destinatário configurado.

## Exemplo de Relatório

O e-mail gerado pelo script tem o seguinte formato:

![](images/image.png)

## Tecnologias Utilizadas

* **Python**
* **`requests`:** Para interagir com a API CoinGecko.
* **`python-dotenv`:** Para gerenciar variáveis de ambiente.
* **`resend`:** Para envio de e-mails.
* **`tasks`:** Para criar atalhos para a execução do código

## Configuração e Instalação

### Pré-requisitos

Certifique-se de ter o **Python** (versão 3.13 ou superior) e o **Poetry** instalados em seu sistema.

### 1. Clonar o Repositório

Comece clonando este projeto para a sua máquina local:

```bash
git clone https://github.com/mateusnoites/coin-report.git
cd coin-report
```

### 2. Variáveis de Ambiente

Crie um arquivo `.env` na raiz do seu projeto (no diretório `coin-report/`) e preencha com suas chaves de API e configurações.

```dotenv
# Chave de API do CoinGecko (versão gratuita/demo)
COINGECKO_KEY="SUA_CHAVE_COINGECKO"

# Chave de API do Resend para envio de e-mails
RESEND_KEY="SUA_CHAVE_RESEND"

# Endereço de e-mail do destinatário do relatório
DESTINATARIO="seu_email@example.com"
```

### 3. Instalação de dependências

Este projeto utiliza o Poetry para gerenciar as dependências.

No diretório raiz do projeto (`coin-report/`), execute o comando para instalar todos os pacotes listados no pyproject.toml e criar o ambiente virtual:
```bash
poetry install
```

### 4. Execução

O projeto inclui um script `taskipy` para facilitar a execução. Para rodar o script de geração e envio do relatório, use:
```bash
task run
```