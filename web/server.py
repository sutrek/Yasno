from flask import Flask, Response, jsonify
from flask_cors import CORS
from sqlalchemy import create_engine, text

connection_string = "mysql+pymysql://std1:123@192.168.50.116:3306/weather"
engine = create_engine(connection_string, echo=True)


app = Flask(__name__)
CORS(app, resources={r"/api/*": {"origins": "*"}})

@app.route("/")
def index():
    return "Hello world"

@app.route("/api/weather/all")
def get_weather():
    with engine.connect() as connection:
        raw_weather = connection.execute(text("SELECT * FROM weather"))
        weather = []
        for r in raw_weather.all():
            weather.append(r._asdict())
        return jsonify(weather)
    return Response(jsonify({"status": "500", "message": "Database is down!"}), status=500)

def main():
    app.run("localhost", 8000, True)

if __name__ == "__main__":
    main()