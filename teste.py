import subprocess
import sys

# Função para instalar pacotes com pip
def install(package):
    subprocess.check_call([sys.executable, '-m', 'pip', 'install', package])

# Tenta importar as bibliotecas necessárias
try:
    import pandas as pd
except ImportError:
    print("Pandas não está instalado. Instalando...")
    install('pandas')
    import pandas as pd

try:
    import mysql.connector
except ImportError:
    print("mysql-connector-python não está instalado. Instalando...")
    install('mysql-connector-python')
    import mysql.connector

try:
    from sqlalchemy import create_engine
except ImportError:
    print("SQLAlchemy não está instalado. Instalando...")
    install('sqlalchemy')
    from sqlalchemy import create_engine

try:
    import openpyxl  # Tenta importar openpyxl para leitura de arquivos Excel
except ImportError:
    print("openpyxl não está instalado. Instalando...")
    install('openpyxl')
    import openpyxl

# Conexão ao banco de dados MySQL
try:
    mydb = mysql.connector.connect(
        host="localhost",  # ou "127.0.0.1"
        user="root",       # seu nome de usuário do MySQL
        password="shinoskun1-T",  # sua senha do MySQL
        database="python_db"  # o nome do banco de dados
    )
    
    print("Conexão bem-sucedida!")

except mysql.connector.Error as err:
    print(f"Erro ao conectar ao MySQL: {err}")
    sys.exit(1)  # Sai do script se a conexão falhar
except Exception as e:
    print(f"Ocorreu um erro inesperado ao conectar: {e}")
    sys.exit(1)

# Criação do cursor
cursor = mydb.cursor()

# Truncar a tabela categoria
try:
    cursor.execute('TRUNCATE TABLE categoria')
    mydb.commit()  
    print("Tabela 'categoria' truncada com sucesso!")
except mysql.connector.Error as err:
    print(f"Erro ao truncar a tabela: {err}")

# Ler dados do Excel
try:
    dados = pd.read_excel(r"c:\Users\Shiry\OneDrive\Área de Trabalho\ETL - GOOGLE BIG QUERY\Arquivos+google+bigquery\Arquivos google bigquery\Arquivos\Origem\arquivos_excel\Categoria.xlsx")
    dados.columns = dados.columns.str.replace("'", "")  # Remove aspas das colunas
    print("Dados lidos com sucesso!")
except Exception as e:
    print(f"Erro ao ler o arquivo Excel: {e}")

# Visualizar os primeiros dados
try:
    print(dados.head(20))
except NameError:
    print("Não foi possível mostrar os dados, pois não foram lidos corretamente.")

# Criar engine do SQLAlchemy e enviar dados para o banco de dados
host = "localhost"
user = "root"
password = "shinoskun1-T"
database = "python_db"

try:
    engine = create_engine(f'mysql+mysqlconnector://{user}:{password}@{host}/{database}')
    dados.to_sql(name='categoria', con=engine, if_exists='replace', index=False)
    print("Dados inseridos na tabela 'categoria' com sucesso!")
except Exception as e:
    print(f"Erro ao inserir dados no MySQL: {e}")

