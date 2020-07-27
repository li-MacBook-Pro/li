from flask import Flask
from flask import request

app = Flask(__name__)
app.route('/')
def index():
    user__agent=request.headers('User-Agent')
    return '<h1>你的browser是%s</h1>'%user__agent

app.route('/')
def abc():
    value = request.args.get("arg")
    return '<h1>arg=%s</h1>'%value

if    __name__=="__min__":
    app.run()