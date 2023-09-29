from flask import Flask, request, render_template
app = Flask(__name__)

@app.route('/')
def index():
    # return '<h1>Hello World!....</h1>'
    return render_template('index.html')

@app.route('/user/<name>')
def user(name):
    # return '<h1>Haloooo {}!</h1>'.format(name)
    return render_template('user.html', name=name)

@app.route('/client/login')
def client_login():
    return render_template('client/login.html')

@app.route('/user-agent')
def useragent():
    user_agent = request.headers.get('User-Agent')
    return '<p>Your browser is {}</p>'.format(user_agent)