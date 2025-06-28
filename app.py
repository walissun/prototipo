import os
from dotenv import load_dotenv
import gspread
from oauth2client.service_account import ServiceAccountCredentials

load_dotenv()  # Carrega variáveis do .env

cred_path = os.getenv("GOOGLE_CREDS")

scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
creds = ServiceAccountCredentials.from_json_keyfile_name(cred_path, scope)
client = gspread.authorize(creds)

# TESTE: tenta abrir uma planilha
try:
    sheet = client.open("cco").sheet1
    print("✅ Autenticação e acesso bem-sucedidos!")
    print("Primeira célula:", sheet.cell(1, 1).value)
except Exception as e:
    print("❌ Erro ao acessar a planilha:")
    print(e)
