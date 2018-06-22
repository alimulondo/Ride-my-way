from flask import Flask
from appv import app
from flask_restful import Resource, Api
from appv.api.offers.view import GetRides,SingleRide,CreateOffer,JoinReq, CloseReq,Acceptreq

# app = Flask(__name__)


# api.add_Resource();
if __name__ == '__main__':

	app.run(port = 5000, debug=True)
