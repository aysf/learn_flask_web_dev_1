from flask import Flask, request
app = Flask(__name__)

@app.route('/')
def index():
    return '<h1>Hello World!....</h1>'

@app.route('/user/<name>')
def user(name):
    return '<h1>Haloooo {}!</h1>'.format(name)

@app.route('/user-agent')
def useragent():
    user_agent = request.headers.get('User-Agent')
    return '<p>Your browser is {}</p>'.format(user_agent)