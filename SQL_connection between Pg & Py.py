# psycopg2 is a popular PostgreSQL adapter for Python.
import psycopg2
# To connect to the db1 database, you use the connect() function of the psycopg2 module. 
conn = psycopg2.connect(
    host="localhost",
    database="db1",          
    user="postgres",     
    password="Tonywld1!"  
)
print("Connect successful")

conn.close()
