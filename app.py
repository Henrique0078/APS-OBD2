from flask import Flask, url_for
from Home.home import home_blueprint
from Dashboard.dashboard import dashboard_blueprint
from ClassificantionIA.classificantionIA import classificantionIA_blueprint
main = Flask(__name__, static_url_path='/static')

main.register_blueprint(home_blueprint, url_prefix="/home")
main.register_blueprint(dashboard_blueprint, url_prefix="/")
main.register_blueprint(classificantionIA_blueprint, url_prefix="/classificantionIA")


#@app.after_request
#def after_request(response):
#     response.header.add("Acess-Control-Allow-Origin", "*")
    
if __name__ == "__main__":
    main.run(debug=True)

