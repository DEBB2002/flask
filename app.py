

from flask import Flask,jsonify, request
app = Flask(__name__)
     

id=0
@app.route('/boo',methods=["GET","POST"])
def mi():
   return "hello"

app.run(host="0.0.0.0",port=5000)