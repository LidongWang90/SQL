import psycopg2

conn = psycopg2.connect(
    host="localhost",
    database="db1",          
    user="postgres",     
    password="Tonywld1!"  
)
print("Connect successful")
cur = conn.cursor()
# call the function in the PostgreSQL
cur.callproc('table_by_age',(2,))

# Get the results of the stored procedure
result = cur.fetchone()
result2 = cur.fetchall()

# Print the results
print(result)
print(result2)

conn.commit()

cur.close()
conn.close()
