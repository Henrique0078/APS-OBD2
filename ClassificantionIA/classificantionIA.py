from flask import Blueprint, render_template
from MachineLearn.machineLearn import train_IA, x_test

classificantionIA_blueprint = Blueprint("classificantionIA", __name__, template_folder="templates")




@classificantionIA_blueprint.route("/")
async def classificantionIA():
    predict = await train_IA()
    return render_template("classificantionIA.html", predict=predict , x_test=x_test)


