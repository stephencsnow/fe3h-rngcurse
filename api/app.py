from flask import Flask, jsonify, request
from flask_cors import CORS
from tinydb import TinyDB, where
from werkzeug.exceptions import BadRequest

from poibin import PoiBin
from dataclasses import fields, asdict

from schemas import Stats, PlayerCharacter, PlayerCharacterSchema, InputSchema

app = Flask(__name__)
CORS(app)

db = TinyDB("data/db.json")


@app.route("/calculate", methods=["POST"])
def calculate():
    marshalled_data = InputSchema().load(request.get_json())

    # populated data
    data = {}

    # populate input
    data["character"] = db.table("characters").get(
        where("name") == marshalled_data.character
    )
    data["stats"] = asdict(marshalled_data.stats)

    current_class_name = None
    data["classes"] = []
    for character_class in marshalled_data.classes:
        data["classes"].append(
            {
                "character_class": db.table("classes").get(
                    where("name") == character_class.name
                ),
                "level_ups": character_class.level_ups,
            }
        )
        if character_class.is_current:
            current_class_name = character_class.name

    if not current_class_name:
        raise BadRequest("Must specify current class")

    data["current_class"] = db.table("classes").get(where("name") == current_class_name)

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
