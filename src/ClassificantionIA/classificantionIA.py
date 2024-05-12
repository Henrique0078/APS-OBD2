from flask import Blueprint, render_template, jsonify

dados = [
    {"id": 1, "nome":"Henrique"},
    {"id": 2, "nome":"Atala"},
    {"id": 3, "nome":"Grasson"}
]

x = [5,4,3,2,1]
y = [1,2,3,4,5]

classificantionIA_blueprint = Blueprint("classificantionIA", __name__, template_folder="templates")

@classificantionIA_blueprint.route("/")
async def classificantionIA():
    return render_template("classificantionIA.html", dados=dados)

@classificantionIA_blueprint.get("/get_data")
def get_data():
    return jsonify({"x": x, "y": y})