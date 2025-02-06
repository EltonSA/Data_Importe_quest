import requests

# Informe o caminho do seu CSV para importar para o bacno de dados
arquivo_csv = "Seu-caminho-csv"

# URL do endpoint de importação, à depender dos criterios criados, podes mudar a porta ou a rota
url = "http://localhost:5177/api/pessoas/importar"

# POST para enviar o arquivo CSV para enviar como parte do corpo da requisição
with open(arquivo_csv, 'rb') as f:
    files = {'file': (arquivo_csv, f, 'text/csv')}
    response = requests.post(url, files=files)

# Verificar se a resposta está OK
if response.status_code == 200:
    print("Importação realizada com sucesso!")
else:
    print(f"Erro: {response.status_code}, {response.text}")
