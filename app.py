import pymysql
import datetime
from flask import Flask,jsonify, request
app = Flask(__name__)
def db_conn():
   conn=None
   try:
      conn=pymysql.connect(

host="sql12.freesqldatabase.com",
database= "sql12529870",
user="sql12529870",
 password="7xMKl6vpJy",

charset="utf8mb4",
cursorclass=pymysql.cursors.DictCursor
) 

   except pymysql.Error as e:
      print(e)
   return conn      

id=0
@app.route("/")
def mai():
   return "hello"
@app.route('/book',methods=["GET","POST"])
def books():
  conn=db_conn()
  cursor=conn.cursor()

  if request.method=="GET"  :
   cursor.execute("SELECT * FROM book ")
   books =[dict(id =row['id'],author=row['author'],lang=row['lang'],title=row['tittle']) for row in cursor.fetchall()]


         
   return jsonify(books)
 

  if request.method=="POST":
   author=request.form["author"]
   lang=request.form["lang"]
  
   title=request.form["title"]
  
   
   sql_stmt='''INSERT INTO book(author,lang,tittle) VALUES(%s,%s,%s)'''
   cursor.execute(sql_stmt,(author,lang,title))
   conn.commit()  
   conn.close  
   time=datetime.datetime.now()
   
   msg="Book with id:",str(cursor.lastrowid),"created sucessfully"
   res={"time":str(time),"msg":str(msg)}
   return jsonify(res),200
if __name__ == "__main__":
   app.run(host="0.0.0.0",port=8080)
