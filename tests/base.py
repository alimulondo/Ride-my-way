"""This modelue holds all the endpoints."""

import unittest
import json
from appv import app
from appv.config import app_config


class BaseTestCase(unittest.TestCase):
    """Class  getting many offers."""

    def create_app(self):
        """Offer is returned here."""
        app.config.from_object(app_config["testing"])
        return app

    def setUp(self):
        """Offer is returned here."""
        self.client = app.test_client(self)
        app.config.from_object(app_config["testing"])

    def tearDown(self):
        """Offer is returned here."""

    def getoneride(self, rideid):
        """Offer is returned here."""
        return self.client.get('/api/v1/rides/{}'.format(rideid),
                               content_type='application/json')

    def get_all_ride(self):
        """Offer is returned here."""
        return self.client.get('/api/v1/rides',
                               content_type='application/json')

    def reqJoiningoffer(self, rideid, dict_cont):
        """Offer is returned here."""
        return self.client.post('/api/v1/rides/{}/requests'.format(rideid),
                                data=json.dumps(dict_cont),
                                content_type='application/json')

    def createoffer(self, info):
        """Offer is returned here."""
        return self.client.post('/api/v1/rides', data=json.dumps(info),
                                content_type='application/json')
