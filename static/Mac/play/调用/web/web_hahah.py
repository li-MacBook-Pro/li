from flask import Flask
from flask import request
from time import *
app = Flask(__name__)

@app.route('/')
def index():
    user_agent = request.headers.get('User-Agent')
    return "<h>%s<h>" %user_agent

@app.route('/abc')
def abc():
    value = request.args.get('arg')
    return "<h>arg = %s<h>" %value

@app.route('/a1')
def a1():
    return "<h>a1<h>"

@app.route('/a2/<aa2>')
def a2(aa2):
    return "<h>"+ aa2 +"<h>"

@app.route('/a3')
def a3():
    return "<h>a3<h>"

@app.route('/')
def a4():
    return "<h>a4<h>"

if __name__ == '__main__':
    app.run()