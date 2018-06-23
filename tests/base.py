import unittest
import json
from appv import app
from appv.config import app_config
# import app


class BaseTestCase(unittest.TestCase):
    def create_app(self):
        """
        Create an instance of the app with the testing configuration
        """
        app.config.from_object(app_config["testing"])
        # app.run(port = 5000)
        # self.client = app.test_client(self)
        # self.app_context.push()

        return app

    def setUp(self):
        #pass
        self.client = app.test_client(self)
        app.config.from_object(app_config["testing"])

    def tearDown(self):
        """
        Drop the data structure data
        """
    # def getsingelride(self):  #, rideid .format(rideid)
    #     return self.client.get('/api/v1/rides', content_type='application/json')
    def getoneride(self, rideid):  #, rideid .format(rideid)
        return self.client.get('/api/v1/rides/{}'.format(rideid), content_type='application/json')

    def getallride(self):  #, rideid .format(rideid)
        return self.client.get('/api/v1/rides', content_type='application/json')


    
    def reqJoiningoffer(self, rideid, dict_cont):
        return self.client.post('/api/v1/rides/{}/requests'.format(rideid), data=json.dumps(dict_cont), content_type='application/json')

    def createoffer(self, info):  #, rideid .format(rideid)
        return self.client.post('/api/v1/rides', data=json.dumps(info),
         content_type='application/json')
