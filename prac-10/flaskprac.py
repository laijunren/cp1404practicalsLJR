from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'


@app.route('/greet')
@app.route('/greet/<name>')
def greet(name=""):
    return "Hello {}".format(name)


# C - Convert Celsius to Fahrenheit
# F - Convert Fahrenheit to Celsius
@app.route('/c')
@app.route('/c/<num>')
def celsius2fahrenheit(num=0):
    celsius = float(num)
    fahrenheit = celsius * 9.0 / 5 + 32
    return "Fahrenheit: {:.2f}".format(fahrenheit)


@app.route('/f')
@app.route('/f/<num>')
def fahrenheit2celsius(num=0):
    fahrenheit = float(num)
    celsius = 5 / 9 * (fahrenheit - 32)
    return "Celsius: {:.2f}".format(celsius)


@app.route('/name')
@app.route('/name/<name>')
def name(name=""):
    return "{}".format(name)


if __name__ == '__main__':
    app.run()
