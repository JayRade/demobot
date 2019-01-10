from flask import Flask, request

app = Flask(__name__)

@app.route('/weather')
def weather():
    weather = request.values.get('text')
    if int(weather) > 30:
        return "it's so hot!"
    else:
        return f'the temperature is {weather}.'


@app.route('/greet', methods=['GET', 'POST'])
def greet_person():
    name = request.values.get('text')
    return f'hi {name}!'


@app.route('/')
def another_word():
    return 'Another word'


@app.route('/ncss')
def ncss_webpage():
    return '<h1> NCSS </h1>'

if __name__ == '__main__':
    app.run()