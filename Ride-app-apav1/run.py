from flask import Flask
from flask_restful import Resource, Api
from appv.api.offers.view import GetRides,SingleRide,CreateOffer,JoinReq, CloseReq,Acceptreq

app = Flask(__name__)

api = Api(app)

api.add_resource(GetRides, '/api/v1/rides')
api.add_resource(SingleRide, '/api/v1/rides/<string:rideid>')
api.add_resource(CreateOffer, '/api/v1/rides')
api.add_resource(JoinReq, '/api/v1/rides/<rideid>/requests')
api.add_resource(CloseReq, '/api/v1/rides/<offerid>/close')
api.add_resource(Acceptreq, '/api/v1/rides/<reqid>/accept')

# api.add_Resource();

app.run(port = 5000)
