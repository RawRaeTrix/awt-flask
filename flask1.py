from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "Welcome to Home Page"

@app.route('/about')
def about():
    return "This is About Page"

@app.route('/user/<name>')
def user(name):
    return f"Hello, {name}!"

if __name__ == '__main__':
    app.run(debug=True)