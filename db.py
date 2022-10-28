import pymysql
 
conn=pymysql.connect(

host="sql12.freesqldatabase.com",
database= "sql12529870",
user="sql12529870",
 password="7xMKl6vpJy",

charset="utf8mb4",
cursorclass=pymysql.cursors.DictCursor
) 


cursor=conn.cursor()

sql_query="""CREATE TABLE book(
    id integer PRIMARY KEY AUTO_INCREMENT,
    author text NOT NULL,
    lang text NOT NULL,
    tittle text NOT NULL

)
"""

cursor.execute(sql_query)
conn.close()