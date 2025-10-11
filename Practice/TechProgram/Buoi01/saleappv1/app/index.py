from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home_page():
    return render_template("index.html")
@app.route('/calculator')
def calculator():
    return render_template('Calculator.html')
@app.route('/hello/<name>')
def hello_word(name):
    return f'hello {name}'


if __name__ == '__main__':
    app.run()