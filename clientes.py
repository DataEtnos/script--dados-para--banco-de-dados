


# %%
import pandas as pd

# %%
import mysql.connector

try:
    # Conexão ao banco de dados MySQL
    mydb = mysql.connector.connect(
        host="localhost",  # ou "127.0.0.1"
        user="root",       # seu nome de usuário do MySQL
        password="shinoskun1-T",  # sua senha do MySQL
        database="python_db"  # o nome do banco de dados
    )
    
    print("Conexão bem-sucedida!")

except mysql.connector.Error as err:
    print(f"Erro ao conectar ao MySQL: {err}")
except Exception as e:
    print(f"Ocorreu um erro inesperado: {e}")


# %%
cursor = mydb.cursor()

# %%
#No banco de dados (clientes) no arquivo em pc Clientes , ou seja no pc C MAISCULO E NO BANCO c minusculo 
cursor.execute('TRUNCATE TABLE clientes')
mydb.commit()  

# %%
dados = pd.read_csv(r"C:/Users/Shiry/OneDrive/Área de Trabalho/ETL - GOOGLE BIG QUERY/Arquivos+google+bigquery/Arquivos google bigquery/Arquivos/Origem/arquivos_csv/Clientes.csv")
str(dados.columns).replace("'","")

# %%
dados.head(20)

# %%
from sqlalchemy import create_engine 
host="localhost"
user="root"
password="shinoskun1-T"
database="python_db"

engine = create_engine(f'mysql+mysqlconnector://{user}:{password}@{host}/{database}')
dados.to_sql(name='clientes', con=engine, if_exists='replace', index=False)


