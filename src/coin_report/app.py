import os
import datetime
import requests
import resend
from schemas import BitcoinSummary
from dotenv import load_dotenv

load_dotenv()

# Configurações básicas - .ENV
destinatario = os.getenv("DESTINATARIO")
resend.api_key = os.getenv("RESEND_KEY")
API_KEY = os.getenv("COINGECKO_KEY")

# Configurações básicas - Constantes
BASE_COIN = 'brl'
URL = f"https://api.coingecko.com/api/v3/coins/markets?ids=bitcoin&vs_currency={BASE_COIN}"

headers = {"x-cg-demo-api-key": f"{API_KEY}"}
res = requests.get(URL, headers=headers).json()[0]

bitcoin = BitcoinSummary(
    preco_atual=res["current_price"],
    diferenca=res["price_change_24h"],
    diferenca_percentual=res["price_change_percentage_24h"]
)

codigo_html = ""

with open("src/coin_report/html/model.html", "r", encoding='utf-8') as arquivo:
    codigo_html = arquivo.read().format(
        condicao = bitcoin.condicao,
        condicao_titulo = bitcoin.condicao.title(),
        emoji_status = ("📈" if bitcoin.condicao == "alta" else "📉"),
        emoji_seta = ("⬆️" if bitcoin.condicao == "alta" else "⬇️"),
        preco_atual = bitcoin.formatar(bitcoin.preco_atual),
        preco_ontem = bitcoin.formatar(bitcoin.preco_ontem),
        porcentagem = bitcoin.abs_porcentagem()
    )

params: resend.Emails.SendParams = {
  "from": "COIN REPORT <no-reply@mabi.allgul.com>",
  "to": [destinatario],
  "subject": f"COIN REPORT ({datetime.datetime.now().date().strftime("%d/%m/%Y")})",
  "html": codigo_html
}

email = resend.Emails.send(params)
print(email)