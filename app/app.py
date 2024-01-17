#!/usr/bin/env python3
from flask import Flask, make_response,jsonify,request
from flask_migrate import Migrate

from models import db, Hero,Power,hero_powers

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

migrate = Migrate(app, db)

db.init_app(app)

@app.route('/')
def home():
    return ''

@app.route('/heroes',methods = ['GET'])
def get_heroes():
    heroes = []
    for hero in Hero.query.all():
        hero_dict = {
            "id": hero.id,
            "name": hero.name,
            "super_name": hero.super_name,
        }
        heroes.append(hero_dict)
    return make_response(jsonify(heroes), 200)

@app.route('/heroes/<int:id>',methods = ['GET'])
def get_heroes_by_id(id):
    hero = Hero.query.filter_by(id=id).first()
    if hero:
        powers = []
        for hero_power in hero_powers.query.filter_by(hero_id = id).all():
            for power in Power.query.filter_by(id = hero_power.power_id):
                power_dict = {
                    "id": power.id,
                    "name": power.name,
                    "description": power.description,
                }
                powers.append(power_dict)
        hero_dict = {
            "id": hero.id,
            "name": hero.name,
            "super_name": hero.super_name,
            "powers": powers
        }
        return make_response(jsonify(hero_dict), 200)
    else:
        error_message = {"error": "Hero not found"}
        return make_response(jsonify(error_message), 404)

@app.route('/powers',methods = ['GET'])
def get_powers():
    powers = []
    for power in Power.query.all():
        power_dict = {
            "id": power.id,
            "name": power.name,
            "description": power.description,
        }
        powers.append(power_dict)
    return make_response(jsonify(powers), 200)

@app.route('/powers/<int:id>',methods = ['GET','PATCH'])
def get_power_by_id(id):
    try:
        power = Power.query.filter_by(id=id).first()
        if power:
            if request.method == 'GET':
                    power_dict = {
                        "id": power.id,
                        "name": power.name,
                        "description": power.description,
                    }
                    return make_response(jsonify(power_dict), 200)

            elif request.method =='PATCH':
                updated_description = request.get_json()
                if updated_description:
                    power.description = updated_description

                db.session.commit()

                new_power = Power.query.filter_by(id=id).first()
                updated_power_dict = {
                        "id": new_power.id,
                        "name": new_power.name,
                        "description": new_power.description,
                    }
                return make_response(jsonify(updated_power_dict),200)
        else:
            error_message = {"error": "Power not found"}
            return make_response(jsonify(error_message), 404)

    except ValueError as e:
        error_message = {
                "errors": ["validation errors"]
            }
        return make_response(jsonify(error_message),400)


@app.route('/hero_powers',methods = ['POST'])
def add_heropower():
    try:
        data = request.get_json()
        new_hp = hero_powers(
            strength = data['strength'],
            hero_id = data['hero_id'],
            power_id = data['power_id'],
        )

        db.session.add(new_hp)
        db.session.commit()

        hero = Hero.query.filter_by(id=new_hp.hero_id).first()
        hero_dict = {
            "id": hero.id,
            "name": hero.name,
            "super_name": hero.super_name,
        }
        powers = []
        for power in Power.query.all():
            if hero_powers.query.filter_by(power_id=power.id).all():
                power_dict ={
                    "id": power.id,
                    "name": power.name,
                    "description": power.description,
                }
                powers.append(power_dict)

        hero_dict["powers"] = powers

        return make_response(jsonify(hero_dict),200)

    except ValueError as e:
        error_message = {"errors": ["validation errors"]}
        return make_response(jsonify(error_message),400)

if __name__ == '__main__':
    app.run(port=5555)


