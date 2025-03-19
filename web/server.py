from flask import Flask, Response
from flask_cors import CORS
import json

app = Flask(__name__)
CORS(app, resources={r"/api/*": {"origins": "*"}})

@app.route("/")
def index():
    return "Hello world"

@app.route("/api/weather/all")
def get_weather():
    weather = [
        {
            "name": "Челябинск",
            "description": "Днем от +2 до +7, ночью до +7°. Гроза. Ожидается легкий бриз, 4 м/с с порывами до 12 м/с. Днем без осадков.",
            "photo": "https://img.freepik.com/premium-vector/dark-clouds-with-lightning-thunderstorm-icon-vector-illustration_566734-74.jpg?w=826",
            "DCF": "22.05.2023"
        },
        {
            "name": "Златоуст",
            "description": "в Златоусте пасмурно, дымка, -4°C. По ощущению -11°C , Ветер 1 м/c.",
            "photo": "https://kartinki.pics/uploads/posts/2022-03/1646329364_1-kartinkin-net-p-kartinki-oblachka-1.png",
            "DCF": "22.05.2023"
        },
        {
            "name": "Миасс",
            "description": "Днем от +4 до +6, ночью до -5°. Гроза. Ожидается легкий бриз, 4 м/с с порывами до 12 м/с. Днем без осадков.",
            "photo": "https://img.freepik.com/premium-vector/dark-clouds-with-lightning-thunderstorm-icon-vector-illustration_566734-74.jpg?w=826",
            "DCF": "22.05.2023"
        },
        {
            "name": "Чебаркуль",
            "description": "в Чебаркуле пасмурно, дымка, -3°C. По ощущению -11°C , Ветер 5 м/c.",
            "photo": "https://kartinki.pics/uploads/posts/2022-03/1646329364_1-kartinkin-net-p-kartinki-oblachka-1.png",
            "DCF": "22.05.2023"
        },
        {
            "name": "Город 5",
            "description": "Днем от +4 до +6, ночью до -5°. Гроза. Ожидается легкий бриз, 4 м/с с порывами до 12 м/с. Днем без осадков.",
            "photo": "https://img.freepik.com/premium-vector/dark-clouds-with-lightning-thunderstorm-icon-vector-illustration_566734-74.jpg?w=826",
            "DCF": "22.05.2023"
        },
           {
            "name": "Город 6",
            "description": "-3°C. По ощущению -11°C , Ветер 5 м/c.",
            "photo": "https://kartinki.pics/uploads/posts/2022-03/1646329364_1-kartinkin-net-p-kartinki-oblachka-1.png",
            "DCF": "22.05.2023"
        },
            {
            "name": "Город 7",
            "description": "Днем от +4 до +6, ночью до -5°. Гроза. Ожидается легкий бриз, 4 м/с с порывами до 12 м/с. Днем без осадков.",
            "photo": "https://img.freepik.com/premium-vector/dark-clouds-with-lightning-thunderstorm-icon-vector-illustration_566734-74.jpg?w=826",
            "DCF": "22.05.2023"
        },
           {
            "name": "Город 8",
            "description": "-3°C. По ощущению -11°C , Ветер 5 м/c.",
            "photo": "https://kartinki.pics/uploads/posts/2022-03/1646329364_1-kartinkin-net-p-kartinki-oblachka-1.png",
            "DCF": "22.05.2023"
        },
        
    ]
    return Response(json.dumps(weather), content_type="application/json") 

def main():
    app.run("localhost", 8000, True)

if __name__ == "__main__":
    main()
