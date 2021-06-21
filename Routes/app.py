from flask import Flask

app = Flask(__name__)

@app.route('/')
@app.route('/home')
def home():
    return 'This is the home page'

@app.route('/about')
def about():
    return 'This is the about page'


@app.route('/squared/<number>')
def squared(number):
    number = int(number)
    result = number * number
    return f'{str(number)} squared is equal to {str(result)}'

if __name__ == "__main__":
    app.run(debug=True)