import psycopg2

connection = psycopg2.connect(
    host="172.19.0.2",
    port="5432",
    user="postgres",
    password="postgres",
    database="postgres"
)
print(connection)
cursor = connection.cursor()
cursor.execute("CREATE TABLE test (id serial PRIMARY KEY, num integer, data varchar);")
cursor.execute("INSERT INTO test (num, data) VALUES (%s, %s)", (100, "abc'def"))
cursor.execute("SELECT * FROM test;")
data =cursor.fetchone()
print(data)
#(1, 100, "abc'def")

# # Make the changes to the database persistent
connection.commit()

# # Close communication with the database
cursor.close()
connection.close()
    