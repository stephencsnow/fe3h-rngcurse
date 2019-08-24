from flask import Flask, jsonify, request
from tinydb import TinyDB, where

from poibin import PoiBin
from dataclasses import fields

from schemas import Stats, PlayerCharacter, PlayerCharacterSchema

app = Flask(__name__)

db = TinyDB("data/db.json")


@app.route("/calculate", methods=["POST"])
def calculate():
    data = request.get_json()

    # populate input
    data["character"] = db.table("characters").get(where("name") == data["character"])
    for character_class in data["classes"]:
        character_class["character_class"] = db.table("classes").get(
            where("name") == character_class["character_class"]
        )
    data["current_class"] = db.table("classes").get(
        where("name") == data["current_class"]
    )

    marshalled_input = PlayerCharacterSchema().load(data)

    res = calc_percentiles(marshalled_input)

    return jsonify(res)


def calc_percentiles(player_character: PlayerCharacter):
    res = {}
    for stat in [f.name for f in fields(Stats)]:
        probs = []
        level_ups = 0
        for c in player_character.classes:
            stat_growth = min(
                [
                    1.0,
                    getattr(player_character.character.growths, stat)
                    + getattr(c.character_class.growths, stat),
                ]
            )
            probs += [stat_growth] * c.level_ups
            level_ups += c.level_ups
        pb = PoiBin(probs)

        growth = (
            getattr(player_character.stats, stat)
            - getattr(player_character.character.base, stat)
            - getattr(player_character.current_class.base, stat)
        )

        res[stat] = dict(
            percentile=pb.cdf(growth) * 100,
            percent_of_level_ups=growth / level_ups * 100,
        )
    return res
