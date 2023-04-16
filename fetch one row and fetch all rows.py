import psycopg2

conn = psycopg2.connect(
    host="localhost",
    database="db1",          
    user="postgres",     
    password="Tonywld1!"  
)
print("Connect successful")
cur = conn.cursor()

# fetch thefirst row 
cur.execute("SELECT * FROM person")  
rows = cur.fetchone()
print(rows)
print(rows[0])

# fetch all rows 
cur.execute("SELECT * FROM person")  
rows = cur.fetchall()
print(rows)
print(rows[0])
print(rows[0][0])

cur.close()
conn.close()
