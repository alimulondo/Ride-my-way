import json
from tests.base import BaseTestCase

class TestCreateoffer(BaseTestCase):
	def test_rideoffer(self):

		with self.client:
			# self.create_app()
			reponse = self.createoffer()
			self.assertEqual(reponse, 300)
