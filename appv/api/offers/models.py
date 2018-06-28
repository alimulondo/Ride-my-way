"""heading.

informatiom.

"""

OFFERS = [
    {
        "id": 101,
        "ownerid": 501,
        "status": 1,
        "offdate": "18/06/2018 10:30Am",
        "offcontent": "AM leaving at 11:00Am and hope to reach at 12:00Pm",
        "offfrom": "Kyenjojo",
        "offto": "mbalala"},
    {
        "id": 102,
        "ownerid": 501,
        "status": 1,
        "offdate": "18/06/2018 10:30Am",
        "offcontent": "AM leaving at 11:00Am and hope to reach at 12:00Pm",
        "offfrom": "Kyenjojo",
        "offto": "mbalala"},
    {
        "id": 103,
        "ownerid": 501,
        "status": 1,
        "offdate": "18/06/2018 10:30Am",
        "offcontent": "AM last here",
        "offfrom": "Busitema",
        "offto": "Kampala"}
]

REQ_LIST = [{
    "reqid": 1000,
    "reqowner": 2000,
    "id": 101,
    "reqdate": "18/06/2018 10:50Am",
    "reqstatus": 0,
    "msg": "can i join you at 11:00am from  masaka? "}
]


def send_data():
    """Offer data is sent from here."""
    return OFFERS


def add_data(data):
    """Offer data is stored from here."""
    OFFERS.append(data)
    return "ok"


# def reqdataSend():
#     """Offer data is sent from here."""
#     return REQ_LIST


def add_request(data):
    """Offer data is sent from here."""
    REQ_LIST.append(data)
    return "ok"


def offer_data():
    """Offer data is sent from here."""
    return OFFERS


def request_data():
    """User requests are sent from here."""
    return REQ_LIST
