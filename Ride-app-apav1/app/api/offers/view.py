"""
  Author: Ali Mulondo
  Date: 18/06/2018
  About:  This file conatians all the end points to the ride offers 
"""
from flask import Flask
from helper import response, resp_for_get_offers, rep_for_single_offer


app = Flask(__name__)

"""
   This is ## GET /rides endpoinf
     """
@app.route('/rides', methods = ['GET'])
def get_Rides():
 	
	return resp_for_get_offers()



@app.route('/rides/<string:rideid>', methods = ['GET'])
def get_single_ride(rideid):

	try:
		int(rideid)
	except ValueError:
		return response("Invalide", "Offer does not exist",rideid)

	else:
		return rep_for_single_offer(rideid)
		# return response("Invalide", "Thats right ",rideid)
	
		


app.run(port = 5000)