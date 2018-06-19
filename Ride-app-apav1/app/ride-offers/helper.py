"""
  Author: Ali Mulondo
  Date: 18/06/2018
  About:  This file connects endpoint logic to dataset. 
"""
from flask import jsonify, make_response
# from app import app
from models import sendData
    
def response(status, msg, code):
	"""
         This is a fallback reponse in case thinges go wrong....
	"""
	jsonvn = jsonify({"status":status, "message":msg, "code":code })

	return make_response(jsonvn) 

def resp_for_get_offers():
	jsonvn = jsonify({"offers": sendData()})
	return make_response(jsonvn)



def rep_for_single_offer(rideid):
	getdata = sendData()
	for content in getdata:
		me = content['offid']
		if content['offid'] == int(rideid.strip()):
			jsonvn = jsonify({"offer": content})

			return make_response(jsonvn)
	# return response("nothin", "jfhfh", me + int(rideid.strip())	)	
	#its for debugging purpose...
	return response("Invalid", "No such offer", 500)	