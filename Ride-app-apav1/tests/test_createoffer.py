import json
from tests.base import BaseTestCase


class TestCreateoffer(BaseTestCase):
	data = [
  {"reqid":1000, "reqowner":2000, "offid":101,
    "reqdate":"18/06/2018 10:50Am", "reqstatus":0,
    "msg":"can i join you at 11:00am from  masaka? " 

  }]
	def test_multrideoffers(self):

		with self.client:
			# self.create_app()
			reponse1 = self.getallride()
			content = (reponse1.get_json())
			msg =content[1]
			code_dict =msg["status"]
			code = code_dict["code"]
			self.assertEqual(code, 100)


	def test_singlerideoffer(self):

		with self.client:
			# self.create_app()
			rideid = 102
			reponse1 = self.getoneride(rideid)
			content = (reponse1.get_json())
			msg =content[1]
			code_dict =msg["status"]
			code = code_dict["code"]
			self.assertEqual(code, 100)

	def test_reqtojoinoffor(self):
		with self.client:
			rideid = 103
			dict_cont = self.data
			reponse1 = self.reqJoiningoffer(rideid,dict_cont)
			content = (reponse1.get_json())

			# code = content["code"]

			self.assertEqual(content["code"], 201)
	def test_creatoffer(self):
		with self.client:
			info = self.data
			reponse1 = self.createoffer(info)
			content = (reponse1.get_json())
			self.assertEqual(content["code"], 201)

