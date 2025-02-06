## 🎯 Objetivo do Projeto
O projeto tem como objetivo desenvolver um sistema em **C#** que importe dados de um arquivo **CSV** para um banco de dados **SQL Server** e forneça um **endpoint** para consulta desses dados no formato **JSON**. Além disso, será desenvolvido um cliente em **Python** para consumir essa API, processar as informações e exibi-las de forma categorizada ao usuário.

## 🛠️ Tecnologias Utilizadas
### Backend (API em C#)
- **ASP.NET Core Web API**
- **Entity Framework Core**
- **SQL Server**
- **CsvHelper** (biblioteca para leitura de arquivos CSV em C#)

### Cliente (Python)
- **Python**
- **Requests** (biblioteca para requisições HTTP)

## 📁 Estrutura do Projeto
```
projeto-raiz/
│
├── api-csharp/                # API desenvolvida em C#
│   ├── Controllers/           # Controladores da API
│   │   ├── PessoasController.cs
│   │
│   ├── Data/                  # Contexto do banco de dados
│   │   ├── AppDbContext.cs
│   │
│   ├── Models/                # Modelos do banco de dados
│   │   ├── Pessoa.cs
│   │
│   ├── Migrations/            # Migrações do Entity Framework
│   ├── appsettings.json       # Configurações da API
│   ├── Program.cs             # Ponto de entrada da aplicação
│   ├── api-csharp.csproj      # Arquivo de configuração do projeto
│
├── cliente-python/            # Cliente Python
│   ├── Importar-csv/          # Scripts de importação CSV
│   │   ├── dados.csv          # Arquivo de exemplo para importação
│   │   ├── importcsv.py       # Script de importação
│   │
│   ├── main.py                # Ponto de entrada do cliente
```

---

## 🚀 Configuração e Execução

### 🔹 Clonando o Repositório
```sh
git clone https://github.com/EltonSA/Data_Importe_quest.git
cd projeto-raiz
```

### 🔹 Configurando e Executando a API em C#
1. **Navegue até o diretório da API:**
   ```sh
   cd api-csharp
   ```
2. **Restaure as dependências do projeto:**
   ```sh
   dotnet restore
   ```
3. **Configure a string de conexão** no arquivo `appsettings.json`:
   ```json
   {
     "ConnectionStrings": {
       "DefaultConnection": "Server=<Local-banco>;Database=<Seu-Banco>;Trusted_Connection=True;TrustServerCertificate=True;"
     },
     "Logging": {
       "LogLevel": {
         "Default": "Information",
         "Microsoft.AspNetCore": "Warning"
       }
     },
     "AllowedHosts": "*"
   }
   ```
4. **Crie a migração inicial para configurar o banco de dados:**
   ```sh
   dotnet ef migrations add InitialCreate
   ```
5. **Atualize o banco de dados aplicando a migração:**
   ```sh
   dotnet ef database update
   ```
6. **Inicie a API:**
   ```sh
   dotnet run
   ```
   A aplicação estará disponível em **https://localhost:5177** (ou **http://localhost:5000** para HTTP).

---

### 🔹 Configurando e Executando o Cliente Python
1. **Navegue até o diretório do cliente:**
   ```sh
   cd cliente-python
   ```
2. **Instale as dependências do projeto:**
   ```sh
   pip install -r requirements.txt
   ```
3. **Execute o script para importar os dados do CSV:**
   Abra o arquivo `importcsv.py` e configure o caminho para o seu arquivo **CSV** e o **endpoint** da API:
   ```python
   import requests

   csv_data = """Id,Nome,Idade,Cidade,Profissao
   1,Ana Silva,29,São Paulo,Engenheira
   2,Bruno Souza,35,Rio de Janeiro,Professor
   3,Carla Mendes,42,Belo Horizonte,Médica
   4,Daniel Santos,27,Curitiba,Desenvolvedor
   5,Elisa Ramos,31,Fortaleza,Advogada
   """

   response = requests.post("http://localhost:5177/api/import", data=csv_data)
   print(response.status_code)
   ```
4. **Execute o script:**
   ```sh
   python importcsv.py
   ```

Agora, os dados estarão importados no banco de dados e poderão ser acessados via API.

---

## 📌 Considerações Finais
Este projeto foi desenvolvido como parte da **Prova Prática IA**, visando demonstrar a integração entre uma **API em C#** e um **cliente em Python**, utilizando **SQL Server** como banco de dados e processamento de arquivos **CSV**.

Caso tenha dúvidas ou sugestões, sinta-se à vontade para contribuir! 🚀

