"""
  Author: Ali Mulondo
  Date: 18/06/2018
  About:  This file conatians all the end points to the ride offers 
"""
from flask import Flask, request
from flask_restful import Resource, Api
# from helper import response, resp_for_get_offers, rep_for_single_offer,do_create
from appv.api.offers.helper import acceptreq, response, resp_for_get_offers, rep_for_single_offer,do_create,can_i_join,closeOffer


app = Flask(__name__)

"""
   This is ## GET /rides endpoinf
     """
class GetRides(Resource):     
# @app.route('/rides', methods = ['GET'])
	def get(self):

		return resp_for_get_offers()



# @app.route('/rides/<string:rideid>', methods = ['GET'])
class SingleRide(Resource):
# def get_single_ride(rideid):
	def get(self,rideid):
		try:
			int(rideid)
		except ValueError:
			return response("Invalide", "Offer does not exist",70)

		else:
			return rep_for_single_offer(rideid)
			# return response("Invalide", "Thats right ",rideid)

# end point for creating a ride offer	
class CreateOffer(Resource):
	def post(self):
		if request.content_type == 'application/json':
				new_content = request.get_json()
		if new_content !="":
			state = do_create(new_content)
			return response("success", "success", 201)
		else:
			return response("failed", "inalide data", 900)	
		


# endpoint for requesting to join a ride

class JoinReq(Resource):
	def post(self, rideid):
		if request.content_type == 'application/json':
				new_content = request.get_json()
				offerid = rideid
		if new_content !="" and offerid !="":
			state = can_i_join(new_content,offerid)
			if state == "ok":
				return response("success", "success", 201)
			else:
				return response("failed", "offer closed", 900)	
		
# its an end point for closing the offer
class CloseReq(Resource):
	def post(self, offerid):
		if offerid !="":
			state = closeOffer(offerid)
			return response("success", "successfully closed", 201)
		# else:
			# return response("failed", "offer closed", 900)	


# its endpoint for accepting a request
class Acceptreq(Resource):
	def post(self, reqid):
		offerid = reqid
		if offerid !="":
			state = acceptreq(offerid)
			if state == "ok":
				return response("success", "Request graanted", 201)
			else:
				return response("failed", "offer closed", 900)	
