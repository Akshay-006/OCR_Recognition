import mysql.connector as db

connection=db.connect(host="localhost",user="root",password="password",database="pdf_to_text")

cursor=connection.cursor()


select_query='''SELECT IF(COUNT(*) > 0, (SELECT MAX(Sno) FROM text), NULL) AS max_sno 
    FROM text'''


cursor.execute(select_query)

result=cursor.fetchone()

S_no=result[0]
if S_no is not None:
    S_no+=1
else:
    S_no=1

row=(S_no,"Hi","Hello")
insert_query="Insert into text values(%s ,%s ,%s)"

print(S_no)

cursor.execute(insert_query,row)
connection.commit()


cursor.close()
connection.close()

if connection.is_connected()==False:
    print("s")
else:
    print("no")

