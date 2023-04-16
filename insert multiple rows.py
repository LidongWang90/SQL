import psycopg2

conn = psycopg2.connect(
    host="localhost",
    database="db1",          
    user="postgres",     
    password="Tonywld1!"  
)
print("Connect successful")
cur = conn.cursor()

# If the table exists, don't need to execute this line. 
# Otherwise, Insert a table into the Postgres and add a row into the table 
# cur.execute("create table person (name text, age int, height real)")

# insert multiple rows:
# ( executemany() method of the cursor object to execute the SQL query with the list of rows. This method takes two arguments: the SQL query as a string, and a list of tuples where each tuple contains the values for a single row.)
name_list = [("Green", 3,125),("Michael", 1,80)]
# cur.executemany("insert into person (name, age, height) values(%s, %s, %s)", (name_list))

# The second way to insert multipal rows:
query = "insert into person (name, age, height) values(%s, %s, %s)"
cur.executemany(query, name_list)

conn.commit()

# fetch thefirst row 
# cur.execute("SELECT * FROM person")  
# rows = cur.fetchone()
# print(rows[0])
cur.close()

conn.close()
