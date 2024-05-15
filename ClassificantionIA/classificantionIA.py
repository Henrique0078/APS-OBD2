from flask import Blueprint, render_template, request, jsonify
from MachineLearn.machineLearn import predict_IA, predict, x_test

classificantionIA_blueprint = Blueprint("classificantionIA", __name__, template_folder="templates")




@classificantionIA_blueprint.route("/")
async def classificantionIA():
    return render_template("classificantionIA.html", predict=predict , x_test=x_test)

@classificantionIA_blueprint.post("/predict")
async def predict_data():
    data = request.json
    predictions = await predict_IA(data)
    return jsonify(predictions.tolist())