from flask import Flask
from flask_restful import Api
from myapi.resources.texts import Texts

app = Flask(__name__)
api = Api(app)

api.add_resource(Texts, '/texts', '/texts/<string:id>')