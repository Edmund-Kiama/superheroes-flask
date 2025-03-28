from flask import request, jsonify, make_response
from models import Hero, HeroPower, Power, db, migrate, app



@app.route("/")
def index():
    return make_response({"message":"app running"}, 200)

@app.route("/heroes", methods=["GET"])
def heroes():
    heroes = Hero.query.all()
    hero_list = []
    for hero in heroes:
        hero_list.append(hero.to_dict(only=["id", "name", "super_name"]))
    return jsonify(hero_list)

@app.route("/heroes/<int:hero_id>", methods=["GET"])
def get_hero(hero_id):
    hero = Hero.query.filter_by(id = hero_id).first()

    if not hero:
        return jsonify({"error": "Hero not found"})
    
    hero_res = hero.to_dict(only=["id", "name", "super_name"])

    hp = HeroPower.query.filter_by(hero_id = hero.id).first()
    hp = hp.to_dict(only=["id", "strength", "hero_id", "power_id"])

    power = Power.query.filter_by(id=hp["power_id"]).first()

    hp["power"] = power.to_dict(only=["id", "name", "description"])
    hero_res["hero_powers"] = hp

    return jsonify(hero_res)

@app.route("/powers", methods=["GET"])
def powers():
    powers = Power.query.all()
    power_list = []
    for power in powers:
        power_list.append(power.to_dict(only=["id", "name", "description"]))
    return jsonify(power_list)

@app.route("/powers/<int:id>", methods=["GET"])
def get_power(id):
    powers = Power.query.filter_by(id=id).first()
    
    if not powers:
        return jsonify({"error":"Power not found"})
    
    return jsonify(powers.to_dict(only=["id", "name", "description"]))

@app.route("/hero-powers")
def hero_powers():
    hero_powers = HeroPower.query.all()
    hero_power_list = []
    for hero_power in hero_powers:
        hero_power_list.append(hero_power.to_dict(only=["id", "strength", "hero_id", "power_id"]))
    return jsonify(hero_power_list)

if __name__=="__main__":
    app.run(debug=True)