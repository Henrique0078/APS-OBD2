from flask import Blueprint, render_template, jsonify

dados = [
    {"id": 1, "nome":"Henrique"},
    {"id": 2, "nome":"Atala"},
    {"id": 3, "nome":"Grasson"}
]

x = [5,4,3,2,1]
y = [1,2,3,4,5]

home_blueprint = Blueprint("home", __name__, template_folder="templates")

@home_blueprint.route("/")
async def home():
    return render_template("home.html", dados=dados)

@home_blueprint.get("/get_data")
def get_data():
    return jsonify({"x": x, "y": y})