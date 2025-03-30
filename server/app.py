from flask import request, jsonify, make_response
from models import Hero, HeroPower, Power, db, migrate, app

@app.route("/")
def index():
    return make_response({"message":"app running"}, 201)


@app.route("/heroes", methods=["GET"])
def heroes():
    heroes = Hero.query.all()
    hero_list = []

    for hero in heroes:
        hero_list.append(hero.to_dict(only=["id", "name", "super_name"]))

    return make_response(hero_list, 201)


@app.route("/heroes/<int:hero_id>", methods=["GET"])
def get_hero(hero_id):
    hero = Hero.query.filter_by(id = hero_id).first()

    if not hero:
        return make_response({"error": "Hero not found"}, 404)
    
    return make_response(hero.to_dict(), 201)


@app.route("/powers", methods=["GET"])
def powers():
    powers = Power.query.all()
    power_list = []

    for power in powers:
        power_list.append(power.to_dict(only=["id", "name", "description"]))

    return make_response(power_list, 201)


@app.route("/powers/<int:id>", methods=["GET"])
def get_power(id):
    powers = Power.query.filter_by(id=id).first()
    
    if not powers:
        return make_response({"error":"Power not found"}, 404)
    
    return make_response(powers.to_dict(only=["id", "name", "description"]), 201)


@app.route("/powers/<int:id>", methods=["PATCH"])
def patch_power(id):
    power = Power.query.get(id)

    if not power:
        return make_response({"error": "Power not found"}, 404)
    
    data = request.get_json()

    if not data:
        return make_response({"error": "Invalid data"}, 400)
    
    if 'description' or 'name' in data:
        if 'name' in data:
            power.name = data["name"]
        else:
            power.description = data["description"]

        db.session.commit()
        return make_response(power.to_dict(only=["id", "name", "description"]), 201)
    else:
        return make_response({"errors": ["validation errors"]}, 400)


@app.route("/hero_powers", methods=["POST"])
def post_hero_power():
    data = request.get_json()
    if not data:
        return make_response( {"errors": "invalid data"}, 400)
    
    try:
        new_hp = HeroPower(
            strength=data["strength"],
            power_id=data["power_id"],
            hero_id=data["hero_id"]
        )
        db.session.add(new_hp)
        db.session.commit()

        # hero = Hero.query.filter_by(id=data["hero_id"]).first()
        # power = Power.query.filter_by(id=data["power_id"]).first()

        # hp_dict = new_hp.to_dict(only=["id", "strength", "hero_id", "power_id"])
        # hp_dict["hero"] = hero.to_dict(only=["id", "name", "super_name"])
        # hp_dict["power"] = power.to_dict(only=["id", "name", "description"])

        # return make_response(hp_dict, 201)
        return make_response(new_hp.to_dict(), 201)
    except KeyError:
        return make_response({"errors": ["validation errors"]}, 400)


if __name__=="__main__":
    app.run(port=5555, debug=True)