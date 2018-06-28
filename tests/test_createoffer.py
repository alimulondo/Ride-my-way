"""This modelue holds all the endpoints."""

from tests.base import BaseTestCase


class TestCreateoffer(BaseTestCase):
    data = [{
        "reqid": 1000,
        "reqowner": 2000,
        "id": 101,
        "reqdate": "18/06/2018 10:50Am",
        "status": 0,
        "msg": "can i join you at 11:00am from  masaka? "
    }]
    data2 = [{
        "reqid": 1002,
        "reqowner": 2000,
        "id": 102,
        "reqdate": "18/06/2018 10:50Am", "status": 0,
        "msg": "can i join you at 11:00am from  masaka? "

    }]

    def test_multrideoffers(self):

        with self.client:
            reponse1 = self.get_all_ride()
            self.assertEqual(reponse1.status_code, 200)

    def test_singlerideoffer(self):

        with self.client:
            rideid = 102
            reponse1 = self.getoneride(rideid)
            self.assertEqual(reponse1.status_code, 200)

    def test_singlerideoffer_strg(self):

        with self.client:
            rideid = 'y102'
            reponse2 = self.getoneride(rideid)
            self.assertEqual(reponse2.status_code, 200)

    def test_reqtojoinoffor(self):
        with self.client:
            rideid = 103
            dict_cont = self.data
            reponse1 = self.reqJoiningoffer(rideid, dict_cont)
            self.assertEqual(reponse1.status_code, 200)

    def test_reqtojoinoffor_cls(self):
        with self.client:
            rideid = 101
            dict_cont = self.data2
            reponse1 = self.reqJoiningoffer(rideid, dict_cont)
            self.assertEqual(reponse1.status_code, 200)

    def test_creatoffer(self):
        with self.client:
            info = self.data
            reponse1 = self.createoffer(info)
            self.assertEqual(reponse1.status_code, 200)

    def test_creatoffer_empty(self):
        with self.client:
            info = ""
            reponse1 = self.createoffer(info)
            self.assertEqual(reponse1.status_code, 200)
