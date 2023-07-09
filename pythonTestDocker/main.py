import requests
from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/")
def show_characters():
    page = request.args.get("page", "1")
    characters = requests.get(
        f"https://rickandmortyapi.com/api/character/?page={page}"
    ).json()
    if "results" in characters:
        return render_template(
            "charactersList.html",
            charactersList=characters["results"],
            page=int(page),
            info=characters["info"],
        )
    else:
        return "<h1>Empty list</h1>"


@app.route("/character/<character_id>")
def show_character(character_id):
    if len(character_id) > 5:
        character_id = character_id.split("_")[1]
    response_character = requests.get(
        f"https://rickandmortyapi.com/api/character/{character_id}"
    ).json()
    return render_template("character.html", character=response_character)


@app.route("/location/<location_id>")
def show_location(location_id):
    location = requests.get(
        f"https://rickandmortyapi.com/api/location/{location_id.split('_')[1]}"
    ).json()

    characters_ids = []
    for character_id in location["residents"]:
        characters_ids.append(int(character_id.split("/")[-1]))

    response_characters = requests.get(
        f"https://rickandmortyapi.com/api/character/{characters_ids}"
    ).json()

    characters = []
    for characters_list in response_characters:
        characters.append(
            {"id": characters_list["id"], "name": characters_list["name"]}
        )

    return render_template("location.html", location=location, characters=characters)


@app.route("/episode/<episode_id>")
def show_episode(episode_id):
    episodies = requests.get(
        f"https://rickandmortyapi.com/api/episode/{episode_id}"
    ).json()

    characters_ids = []
    for character_id in episodies["characters"]:
        characters_ids.append(int(character_id.split("/")[-1]))

    response_characters = requests.get(
        f"https://rickandmortyapi.com/api/character/{characters_ids}"
    ).json()

    characters = []
    for characters_list in response_characters:
        characters.append(
            {"id": characters_list["id"], "name": characters_list["name"]}
        )

    return render_template("episode.html", episode=episodies, characters=characters)
