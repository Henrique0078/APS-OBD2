from flask import Blueprint, render_template, jsonify

dados = [
    {"id": 1, "nome":"Henrique"},
    {"id": 2, "nome":"Atala"},
    {"id": 3, "nome":"Grasson"}
]

x = [5,4,3,2,1]
y = [1,2,3,4,5]

graphsExplanation_blueprint = Blueprint("graphsExplanation", __name__, template_folder="templates")

@graphsExplanation_blueprint.route("/")
async def graphsExplanation():
    return render_template("graphsExplanation.html", dados=dados)

@graphsExplanation_blueprint.get("/get_data")
def get_data():
    return jsonify({"x": x, "y": y})