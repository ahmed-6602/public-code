import mysql.connector  

myconn = mysql.connector.connect(host = "localhost", user = "root",passwd = "Ahmed@6602", database="StudentsDB")

cur = myconn.cursor()

cur.execute("select * from students")

result = cur.fetchall()
print("Student Details are :")

for x in result:
	print(x);

myconn.commit()

myconn.close()
