import mysql.connector

conn = mysql.connector.connect(username='root', password='vrma@2001',host='localhost',database='face_recognizer',port=3306)
cursor = conn.cursor()

cursor.execute("show databases")

data = cursor.fetchall()

print(data)

conn.close()