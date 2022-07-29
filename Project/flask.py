import pandas as pd 
from flask import Flask, jsonify, request
from data import data
stars_data_rows=[]
final_dict=[]

final_planet_list=[]
for stars_data in stars_data_rows:
  temp_dict={
      "name": stars_data[1],
      "distance_from_earth": stars_data[2],
      "planet_mass": stars_data[3],
      "planet_type": stars_data[6],
      "planet_radius": stars_data[7],
      "distance_from_their_sun":stars_data[8],
      "orbital_period": stars_data[9],
      "gravity": stars_data[18],
      "orbital_speed":stars_data[19]
  }

  temp_dict["specifications"]=final_dict[stars_data[1]]
  final_planet_list.append(temp_dict)

print(final_planet_list)

app = Flask(__name__)

@app.route("/")
def index():
    return jsonify({
        "data": data,
        "message": "success"
    }), 200

@app.route("/planet")
def planet():
    name = request.args.get("name")
    planet_data = next(item for item in data if item["name"] == name)
    return jsonify({
        "data": planet_data,
        "message": "success"
    }), 200

if __name__ == "__main__":
    app.run()