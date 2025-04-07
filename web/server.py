from flask import Flask, Response, jsonify,request
from flask_cors import CORS
from sqlalchemy import create_engine, text, bindparam

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
 

@app.route("/api/weather", methods=["POST"])
def add_product():
    if request.method == "POST":
        form = request.form
        with engine.connect() as connection:
            query = text("INSERT INTO weather (city, Temperature, falllout, photo) VALUES (:city, :Temperature, :falllout, :photo) RETURNING *")
            query = query.bindparams(bindparam("city", form.get("city")))
            query = query.bindparams(bindparam("Temperature", form.get("Temperature")))
            query = query.bindparams(bindparam("falllout", form.get("falllout")))
            query = query.bindparams(bindparam("photo", form.get("photo")))
            result = connection.execute(query)
            connection.commit()
            return jsonify(result.fetchone()._asdict())
        return jsonify({"message": "Error"})


def main():
    app.run("localhost", 8000, True)

if __name__ == "__main__":
    main()