"""
  Author: Ali Mulondo
  Date: 18/06/2018
  About:  This file connects endpoint logic to dataset. 
"""
from flask import jsonify, make_response, request
# from app import app
# from models import sendData, addData,reqdataAdd
from appv.api.offers.models import retreqData, retData, sendData, addData,reqdataAdd
    
def response(status, msg, code):
	"""
         This is a fallback reponse in case thinges go wrong....
	"""
	jsonvn = jsonify({"status":status, "message":msg, "code":code })

	return make_response(jsonvn) 

def resp_for_get_offers():
	sucess = {"status":"sucess", "code":100}
	jsonvn = jsonify({"offers": sendData()}, {"status": sucess})
	return make_response(jsonvn)



def rep_for_single_offer(rideid):
	getdata = sendData()
	for content in getdata:
		# me =  content['offid']
		if content['offid'] == int(rideid.strip()):
			sucess = {"status":"sucess", "code":100}
			jsonvn = jsonify({"offer": content}, {"status": sucess})

			return make_response(jsonvn)
	# return response("nothin", "jfhfh", me + int(rideid.strip())	)	
	#its for debugging purpose...
	return response("Invalid", "No such offer", 500)

def do_create(data):
	new_dict = data     
	  # {"offer": data}
	# add new offer to memory
	state = addData(new_dict)

	if state == "ok":
		return "done"
	else: return "issues"
def can_i_join(new_content,offerid):
	try:
		realval = int(offerid.strip())
	except ValueError:
		return response("Invalide", "Offer does not exist",rideid)
	else:
		for cont in retData():
			if cont["offid"]==realval and cont["offstatus"] == 1:
				reqdataAdd(new_content)
				return "ok"
			# else:


def closeOffer(offerid):
	try:
		realval = int(offerid.strip())
	except ValueError:
		return response("Invalide", "Offer does not exist",rideid)
	else:
		for cont in retData():
			if cont["offid"]  == realval:
				cont["offstatus"] = 0
				return "ok"
			else:
				response("Error", "Failed to close", 700)	

def acceptreq(reqid):
	try:
		offerid = reqid
		realval = int(offerid.strip())
	except ValueError:
		return response("Invalide", "Offer does not exist",rideid)
	else:
		for cont in retreqData():
			if cont["reqid"]  == realval:
				cont["reqstatus"] = 1
				return "ok"
