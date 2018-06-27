
import json
from tests.base import BaseTestCase


class TestCreateoffer(BaseTestCase):
	data = [
  {"reqid":1000, "reqowner":2000, "offid":101,
    "reqdate":"18/06/2018 10:50Am", "reqstatus":0,
    "msg":"can i join you at 11:00am from  masaka? " 
    }]
	data2 = [
  {"reqid":1002, "reqowner":2000, "offid":102,
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
			# checking if a non string is passed as an offer variable
	def test_singlerideoffer_strg(self):

		with self.client:
			# self.create_app()
			rideid = 'y102'
			reponse2 = self.getoneride(rideid)
			content = (reponse2.get_json())
			# msg =content[1]
			# code_dict =msg["status"]
			code = content["code"]
			self.assertEqual(code, 70)
			# checking if a non string is passed as an offer variable
			


	def test_reqtojoinoffor(self):
		with self.client:
			rideid = 103
			dict_cont = self.data
			reponse1 = self.reqJoiningoffer(rideid,dict_cont)
			content = (reponse1.get_json())

			# test try to join a clsed offer
	def test_reqtojoinoffor_cls(self):
		with self.client:
			rideid = 101
			dict_cont = self.data2
			reponse1 = self.reqJoiningoffer(rideid,dict_cont)
			content = (reponse1.get_json())
			self.assertEqual(content["code"], 900)

	def test_creatoffer(self):
		with self.client:
			info = self.data
			reponse1 = self.createoffer(info)
			content = (reponse1.get_json())
			self.assertEqual(content["code"], 201)

			# test creating offer with zero content
	def test_creatoffer_empty(self):
		with self.client:
			info = ""
			reponse1 = self.createoffer(info)
			content = (reponse1.get_json())
			self.assertEqual(content["code"], 900)

