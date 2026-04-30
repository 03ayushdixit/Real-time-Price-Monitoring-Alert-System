import mysql
import mysql.connector as sql

db=sql.connect(
    host="localhost",
    user="root",
    password="password",
    use_pure=True
)
cr= db.cursor()
cr.execute("show databases")
for i in cr:
    print(i)










