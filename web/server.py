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
def add_weather():
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
    
@app.route("/api/weather/<id>", methods=["GET", "DELETE", "PUT"])
def weather(id: int):
    if request.method == "GET":
        with engine.connect() as connection:
            query = text("SELECT * FROM weather WHERE id = :id")
            query = query.bindparams(bindparam("id", id))
            result = connection.execute(query)
            return jsonify(result.fetchone()._asdict())
        return jsonify({"message": "Error"})
    
    if request.method == "DELETE":
        with engine.connect() as connection:
            query = text("DELETE FROM weather WHERE id = :id;")
            query = query.bindparams(bindparam("id", id))
            result = connection.execute(query)
            connection.commit()
            return jsonify({"message": "Success", "id": id})
        return jsonify({"message": "Error"})
 
    if request.method == "PUT":
        form = request.form
        with engine.connect() as connection:
            query = text("UPDATE weather SET city = :city, Temperature = :Temperature, falllout = :falllout, photo = :photo WHERE id = :id")
            query = query.bindparams(bindparam("city", form.get("city")))
            query = query.bindparams(bindparam("Temperature", form.get("Temperature")))
            query = query.bindparams(bindparam("falllout", form.get("falllout")))
            query = query.bindparams(bindparam("photo", form.get("photo")))
            query = query.bindparams(bindparam("id", id))
            connection.execute(query)
            connection.commit()
 
            query = text("SELECT * FROM weather WHERE id = :id")
            query = query.bindparams(bindparam("id", id))
            result = connection.execute(query)
            return jsonify(result.fetchone()._asdict())
        return jsonify({"message": "Error"})
 

def main():
    app.run("localhost", 8000, True)

if __name__ == "__main__":
    main()