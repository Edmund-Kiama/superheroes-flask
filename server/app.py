from flask import request, jsonify, make_response
from models import Hero, HeroPower, Power, db, migrate, app



@app.route("/")
def index():
    return make_response({"message":"app running"}, 200)

@app.route("/heroes")
def heroes():
    heroes = Hero.query.all()
    hero_list = []
    for hero in heroes:
        hero_list.append(hero.to_dict(only=["id", "name", "super_name"]))
    return jsonify(hero_list)

@app.route("/powers")
def powers():
    powers = Power.query.all()
    power_list = []
    for power in powers:
        power_list.append(power.to_dict(only=["id", "name", "description"]))
    return jsonify(power_list)

@app.route("/hero-powers")
def hero_powers():
    hero_powers = HeroPower.query.all()
    hero_power_list = []
    for hero_power in hero_powers:
        hero_power_list.append(hero_power.to_dict(only=["id", "strength", "hero_id", "power_id"]))
    return jsonify(hero_power_list)

if __name__=="__main__":
    app.run(debug=True)