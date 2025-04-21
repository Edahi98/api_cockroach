from flask import Flask
from .api_flask import api
from flask_cors import CORS

app = Flask(__name__)
CORS(app,  resources={"*": {"origins": "*"}})
app.register_blueprint(api)


