from flask import Flask, url_for, request, json
from markupsafe import escape
from flask import render_template

app = Flask(__name__)

@app.route('/')
def index():
    return 'index'

@app.route('/shopping')
def shopping():
    food = ["Chees", "Tuna", "Beef"]
    return render_template('shopping.html', food = food)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        return 'do the login'
    else:
        return 'show the login form'

@app.route('/create/<username>', methods=['GET', 'POST'])
def create(username):
    if request.method == 'POST':
        
        data = json.loads(request.data)
        email = data["emailId"]
        return 'do the login' + str(request.json)

    else:
        return 'show the login form' + str(request.data)

@app.route('/user/<username>')
def profile(username):
    return '{}\'s profile'.format(escape(username))

with app.test_request_context():
    print(url_for('index'))
    print(url_for('login'))
    print(url_for('login', next='/'))
    print(url_for('profile', username='John Doe'))


if __name__ == '__main__':
    app.run()