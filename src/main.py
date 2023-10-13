from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/',methods = ['GET'])
def home():
     return "Hello Word"


app.run(port = 5000, host='localhost', debug = True)