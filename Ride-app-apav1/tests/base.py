import unittest
import json
from appv import app
# import app


class BaseTestCase(unittest.TestCase):
    def create_app(self):
        """
        Create an instance of the app with the testing configuration
        """
        app.config.from_object(app_config["testing"])
        return app

    def setUp(self):
        #pass
        self.client = app.test_client(self)

    def tearDown(self):
        """
        Drop the data structure data
        """
    def getsingelride(self):  #, rideid .format(rideid)
        return self.client.get('/api/v1/rides', content_type='application/json')

 