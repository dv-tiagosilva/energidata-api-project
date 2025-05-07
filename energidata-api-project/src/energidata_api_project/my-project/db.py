import psycopg2
from dotenv import load_dotenv
import os
from ingestor import get_filtered_data

# Information keys
load_dotenv()
host = os.getenv("DB_HOST")
dbname = os.getenv("DB_NAME")
user = os.getenv("DB_USER")
password = os.getenv("DB_PASSWORD")

# Getting the data from "ingestor.py" file
data_filtered = get_filtered_data()

# Transform the data into a sequence of tuples, so we can use executemany() function from psycopg2
data_to_insert = []
for d in data_filtered:
    try:
        data_to_insert.append((
            d["MinutesUTC"],
            d["Price_area"],
            d["CO2_emission"]
        ))
    except KeyError as e:
        print(f"Erro: chave ausente {e} em {d}")


if data_filtered:
    try:
        conn = psycopg2.connect(
            host=host,
            dbname=dbname,
            user=user,
            password=password
        )
        
        # Creating a cursor
        cursor = conn.cursor()

        # Definning query
        query = """
        INSERT INTO energi_db (minutes_utc, price_area, co2_emission)
        VALUES (%s, %s, %s);
        """
        # Dados a serem inseridos
        dados = ('valor1', 'valor2', 'valor3')

        # Executando a query
        cursor.executemany(query, data_to_insert)

        # Commit para salvar as alterações no banco de dados
        conn.commit()
        print("Data entered successfully!")
        
    except Exception as e:
        print(f"Error: {e}")

    finally:
        #Closing cursor and connection
        if cursor:
            cursor.close()
        if conn:
            conn.close()

else: 
    print("No data to insert")