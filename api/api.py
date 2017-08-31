from flask import Flask 
from flask_restful import Api, Resource, reqparse 

app = Flask(__name__)
api = Api(app)

class EchoApi(Resource):
	def get(self, value):
		return {'hello': value}

api.add_resource(EchoApi, '/echo/<value>', endpoint = 'echo')

if __name__ == '__main__':
	app.run
