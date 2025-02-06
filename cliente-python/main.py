import requests

# Função para categorizar a pessoa com base na idade
def categorizar_idade(idade):
    if idade < 30:
        return "Jovem"
    elif 30 <= idade <= 40:
        return "Adulto"
    else:
        return "Sênior"

# Input para informar o id de consulta
id_user = input("Informe o ID do usuário (Apenas número): ")

# Verifica se o ID é numérico
if id_user.isdigit():
    id_user = int(id_user)
    
    # Função para consultar a API C#
    def consultar_pessoa(id):
        url = f'http://localhost:5177/api/pessoas/{id}'  # URL da API C#
        response = requests.get(url)
        
        if response.status_code == 200:
            pessoa = response.json()
            idade_categoria = categorizar_idade(pessoa['idade'])
            print(f"Nome: {pessoa['nome']}")
            print(f"Idade: {pessoa['idade']} ({idade_categoria})")
            print(f"Cidade: {pessoa['cidade']}")
            print(f"Profissão: {pessoa['profissao']}")
        else:
            print("Pessoa não encontrada!")
    
    # Chamada da função com o ID informado pelo usuário
    consultar_pessoa(id_user)
else:
    print("ID inválido! Por favor, informe um número.")