"""This modelue holds all the endpoints."""
from flask import Flask, request

from flask_restful import Resource

from appv.api.offers.helper import accept_request, response, \
    resp_for_get_offers, rep_for_single_offer, \
    do_create, can_i_join, close_offer


app = Flask(__name__)


class GetRides(Resource):
    """Class  getting many offers."""

    def get(self):
        """Offer is returned here."""
        return resp_for_get_offers()


class SingleRide(Resource):
    """Class  getting singel offer."""

    def get(self, rideid):
        """Offer is returned here."""
        try:
            int(rideid)
        except ValueError:
            return response("Invalide", "Offer does not exist", 70)
        else:
            return rep_for_single_offer(rideid)


class CreateOffer(Resource):
    """Class  for creating offers."""

    def post(self):
        """Offer storage is done here."""
        if request.content_type == 'application/json':
            new_content = request.get_json()
        if new_content != "":
            state = do_create(new_content)
            if state == "done":
                return response("success", "success", 201)
            return response("failed", "failed", state)


class JoinReq(Resource):
    """Class  for requeting to join an offer."""

    def post(self, rideid):
        """Request processing is done here."""
        if request.content_type == 'application/json':
            new_content = request.get_json()
            offerid = rideid
        if new_content != "" and offerid != "":
            state = can_i_join(new_content, offerid)
            if state == "ok":
                return response("success", "success", 201)
            else:
                return response("failed", "offer closed", state)


class CloseReq(Resource):
    """Class  for closing an offer."""

    def post(self, offerid):
        """Offer closing is done here."""
        if offerid != "":
            state = close_offer(offerid)
            if state == "ok":
                return response("success", "successfully closed", 201)


class Acceptreq(Resource):
    """Class  for accepting a request."""

    def post(self, reqid):
        """Request acceptence is done here."""
        offerid = reqid
        if offerid != "":
            state = accept_request(offerid)
            if state == "ok":
                return response("success", "Request graanted", 201)
            return response("failed", "offer closed", 900)
