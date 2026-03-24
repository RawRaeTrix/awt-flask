from flask import Flask
app = Flask(__name__)

@app.route('/')
def index():
    return '<h1>Hello from index</h1>'

@app.route('/about')
def about():
    return '<h1>Hello from about</h1>'

@app.route('/contact')
def contact():
    return '<h1>Hello from contact</h1>'

@app.route('/')
@app.route('/home')
@app.route('/index')
def home():
    return 'Welcome Home!'


if __name__ == '__main__':
    app.run(debug=True, use_reloader=False)

    