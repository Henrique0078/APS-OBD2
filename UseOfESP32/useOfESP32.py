from flask import Blueprint, render_template, jsonify

dados = [
    {"id": 1, "nome":"Henrique"},
    {"id": 2, "nome":"Atala"},
    {"id": 3, "nome":"Grasson"}
]

x = [5,4,3,2,1]
y = [1,2,3,4,5]

useOfESP32_blueprint = Blueprint("useOfESP32", __name__, template_folder="templates")

@useOfESP32_blueprint.route("/")
async def useOfESP32():
    return render_template("useOfESP32.html", dados=dados)

@useOfESP32_blueprint.get("/get_data")
def get_data():
    return jsonify({"x": x, "y": y})