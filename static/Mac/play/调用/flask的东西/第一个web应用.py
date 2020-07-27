from flask import Flask
from time import*
app=Flask(__name__)
@app.route('/')
def helloworld():
    return strftime('%Y-%m-%d %H:%M:%S',localtime(time()))
@app.route('/')
def index():
    return '<h1>root</h1>'

# @app.route('//')
if __name__=='_main_':
    app.run()