from flask import Blueprint, request, jsonify
from mongo_client import mongo
from models import create_hero_document
import os

routes = Blueprint('routes', __name__)
client = mongo
db = client["comics"]

@routes.route("/heroes", methods=["GET"])
def get_heroes():
    universe = request.args.get("universe")
    query = {"universe": universe} if universe else {}
    heroes = list(db.heroes.find(query, {"_id": 0}))
    return jsonify(heroes)

@routes.route("/hero/<name>", methods=["GET"])
def get_hero(name):
    hero = db.heroes.find_one({"name": name}, {"_id": 0})
    return jsonify(hero) if hero else ("", 404)

@routes.route("/hero", methods=["POST"])
def create_hero():
    data = request.json
    print(data)
    if db.heroes.find_one({"name": data["name"]}):
        return jsonify({"error": "Hero already exists"}), 400
    db.heroes.insert_one(create_hero_document(data))
    return jsonify({"message": "Hero created"}), 201

@routes.route("/hero/<name>", methods=["PUT"])
def update_hero(name):
    data = request.json
    result = db.heroes.update_one({"name": name}, {"$set": data})
    return jsonify({"message": "Updated"}) if result.modified_count else ("", 404)

@routes.route("/hero/<name>", methods=["DELETE"])
def delete_hero(name):
    print(f"Deleting hero: {name}")
    result = db.heroes.delete_one({"name": name})
    return jsonify({"message": "Deleted"}) if result.deleted_count else ("", 404)
