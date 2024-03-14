import mysql.connector

# establish connection 

connection = mysql.connector.connect(host="localhost",user="root",password="",database="testt")

cur = connection.cursor(buffered=True)


if connection.is_connected():
  print("connection ss")
else:
  print("lol")

  #operation on database
try:
  cur.execute("use registration")
except:
  cur.execute("create database registration")
  cur.execute("use registration")

try:
  cur.execute("describe persons")
except:
  cur.execute("create table persons( id int primary key auto_increment, name varchar(20))")

sql = "INSERT INTO persons (name) VALUES (%s)"
val = ("john",)

try:
    # Execute SQL statement
    cur.execute(sql, val)
    
    # Commit the transaction
    connection.commit()
    
    print("Record inserted successfully.")
except mysql.connector.Error as err:
    # Handle any errors
    print("Error:", err)
finally:
    # Close cursor and connection
    cur.close()
    connection.close()

