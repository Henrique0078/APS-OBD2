from flask import Flask
from src.Home.home import home_blueprint
app = Flask(__name__)

app.register_blueprint(home_blueprint, url_prefix="/home")


@app.after_request
def after_request(response):
    response.header.add("Acess-Control-Allow-Origin", "*")
    
if __name__ == "__main__":
    app.run(debug=True)