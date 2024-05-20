from flask import Flask, url_for
from Home.home import home_blueprint
from Dashboard.dashboard import dashboard_blueprint
from ClassificantionIA.classificantionIA import classificantionIA_blueprint
from MachineLearn.metrics import metrics_blueprint
from GraphsExplanation.graphsExplanation import graphsExplanation_blueprint  
from UseOfESP32.useOfESP32 import useOfESP32_blueprint 
from OBDIIDescription.obdIIDescription import obdIIDescription_blueprint 
from GateawayUseSimulationResults.gateawayUseSimulationResults import gateawayUseSimulationResults_blueprint

main = Flask(__name__, static_url_path='/static')

main.register_blueprint(home_blueprint, url_prefix="/home")
main.register_blueprint(dashboard_blueprint, url_prefix="/")
main.register_blueprint(classificantionIA_blueprint, url_prefix="/classificantionIA")
main.register_blueprint(metrics_blueprint, url_prefix="/metrics")  
main.register_blueprint(graphsExplanation_blueprint, url_prefix="/graphsExplanation")
main.register_blueprint(useOfESP32_blueprint, url_prefix="/useOfESP32")
main.register_blueprint(obdIIDescription_blueprint, url_prefix="/obdIIDescription") 
main.register_blueprint(gateawayUseSimulationResults_blueprint, url_prefix="/gateawayUseSimulationResults") 






#@app.after_request
#def after_request(response):
#     response.header.add("Acess-Control-Allow-Origin", "*")
    
if __name__ == "__main__":
    main.run(debug=True)

