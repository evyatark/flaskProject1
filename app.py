from flask import Flask
from flask import url_for
from markupsafe import escape


app = Flask(__name__)

# see https://flask.palletsprojects.com/en/2.2.x/quickstart/


@app.route('/')
def hello_world():  # put application's code here
    return 'Hello World!'


@app.route('/hello')
def hello_world_2():  # put application's code here
    return '<h1>Hello World!!</h1>'


@app.route('/user/<username>')
def show_user_profile(username):
    # show the user profile for that user
    return f'User is {escape(username)}'


with app.test_request_context():
    print(url_for('hello_world'))
    print(url_for('hello_world_2'))
    print(url_for('show_user_profile', username='Evyatar'))

if __name__ == '__main__':
    app.run()
