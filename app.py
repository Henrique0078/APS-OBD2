from flask import Flask
from src.Home.home import home_blueprint
from src.Dashboard.dashboard import dashboard_blueprint
from src.ClassificantionIA.classificantionIA import classificantionIA_blueprint
main = Flask(__name__)

main.register_blueprint(home_blueprint, url_prefix="/home")
main.register_blueprint(dashboard_blueprint, url_prefix="/")
main.register_blueprint(classificantionIA_blueprint, url_prefix="/classificantionIA")


#@app.after_request
#def after_request(response):
#     response.header.add("Acess-Control-Allow-Origin", "*")
    
if __name__ == "__main__":
    main.run(debug=True)

