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

# This is the function in the Pg:
'''
CREATE or replace FUNCTION table_by_age (x INTEGER)
RETURNS table(name text,
    age integer,
    height real)
AS $$
BEGIN
    return query
	select person.name, person.age, person.height
	from person 
	where person.age = x;
END;
$$ 
LANGUAGE plpgsql;
'''