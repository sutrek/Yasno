from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return "hello world"
    return render_template('index.html')

@app.route('/api/weather/all')
def get_weather():
    weather = [
        {
            "name": "Златоуст"
            "temperature": "-3"
            "state": "Облачно"
        },
        {
            "name": "Челябинск"
            "temperature": "-2"
            "state": "Облачно с прояснением"
        },
        {
            "name": "Миасс"
            "temperature": "-5"
            "state": "Пасмурно"
        },
        {
            "name": "Чебаркуль"
            "temperature": "-1"
            "state": "Ясно"
        },
    ]

def main():
    app.run("localhost", 8000, True)

if __name__=='__main__':
    main()