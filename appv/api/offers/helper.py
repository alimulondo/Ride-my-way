"""Helper.

Puts together loic for the views.

"""

from flask import jsonify, make_response

from appv.api.offers.models import request_data, offer_data, send_data, \
    add_data, add_request


def response(status, msg, code):
    """General reponse message function."""
    jsonvn = jsonify({"status": status, "message": msg, "code": code})
    return make_response(jsonvn)


def resp_for_get_offers():
    """Returning offers."""
    sucess = {"status": "sucess", "code": 100}
    jsonvn = jsonify({"offers": send_data()}, {"status": sucess})
    return make_response(jsonvn)


def rep_for_single_offer(rideid):
    """General reponse message function."""
    getdata = send_data()
    for content in getdata:
        if content['id'] == int(rideid.strip()):
            sucess = {"status": "sucess", "code": 100}
            jsonvn = jsonify({"offer": content}, {"status": sucess})

            return make_response(jsonvn)
    return response("Invalid", "No such offer", 500)


def do_create(data):
    """General reponse message function."""
    new_dict = data
    state = add_data(new_dict)

    if state == "ok":
        return "done"
    return "hfgf"


def can_i_join(new_content, offerid):
    """Request proccessing is done here."""
    try:
        realval = int(offerid.strip())
    except ValueError:
        return response("Invalide", "Offer does not exist", 800)
    else:
        for cont in offer_data():
            if cont["id"] == realval and cont["status"] == 1:
                add_request(new_content)
                return "ok"
        return cont["id"]


def close_offer(offerid):
    """Close offer processing."""
    try:
        realval = int(offerid.strip())
    except ValueError:
        return response("Invalide", "Offer does not exist", 800)
    else:
        for cont in offer_data():
            if cont["id"] == realval:
                cont["status"] = 0
                return "ok"
            return response("Error", "Failed to close", 700)


def accept_request(reqid):
    """Request acceptencen is processed here."""
    try:
        offerid = reqid
        realval = int(offerid.strip())
    except ValueError:
        return response("Invalide", "Offer does not exist", 800)
    else:
        for cont in request_data():
            if cont["reqid"] == realval:
                cont["status"] = 1
                return "ok"
            return "not"
