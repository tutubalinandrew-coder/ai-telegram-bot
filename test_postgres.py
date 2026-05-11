from postgres_database import connect_postgres


connection = connect_postgres()
print("PostgreSQL connected")
connection.close()