import psycopg2

conn = psycopg2.connect(
    host="localhost",
    database="db1",          
    user="postgres",     
    password="Tonywld1!"  
)
print("Connect successful")
cur = conn.cursor()

# Insert a table into the db1 of PostgreSQL
# after excute the below line once, we cannot excute it again, since the table already created.
# cur.execute("create table person (name text, age int, height real)")

# The first way to insert only one row:
# cur.execute("insert into person (name, age, height) values(%s, %s, %s)", ('Lee', 32, 170))

# The second way to insert only one row:
query = "insert into person (name, age, height) values(%s, %s, %s)"
cur.execute(query, ('Lidong', 33, 170))
# call conn.commit() to commit the transaction and save the changes to the database
conn.commit()
# close the cursor and the connection using the close() method for several reasons: 
# 1. Free up resources: The cursor and the connection objects use system resources, 
#    such as memory and network connections. 
#    If you don't close them properly, these resources may not be released until the Python interpreter exits. 
#    Closing them properly with close() ensures that the resources are released immediately after you finish using them. 
# 2. Release locks: When you execute a SQL query using a cursor, the database may acquire a lock on the underlying data. 
#    If you don't close the cursor properly, the lock may be held indefinitely, causing other queries to wait. 
#    Closing the cursor with close() releases the lock. 
# 3. Transaction management: In some cases, the cursor may be used in a transaction. 
#    If you don't close the cursor properly, the transaction may be left open, 
#    which can lead to unexpected behavior in the database.
# 4. Performance: Leaving cursors and connections open when they're no longer needed can have a negative impact on performance. 
#    Closing them properly with close() helps to optimize the performance of your Python program. 
cur.close()
conn.close()
