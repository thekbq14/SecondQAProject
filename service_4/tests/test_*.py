from flask_testing import TestCase

from application import app, db
from service_4.app import app

from flask import redirect, url_for

class TestBase(TestCase):
    def create_app(self):
        
        return app
    

class TestResponse(TestBase):
    def test_get_city(self):
        response = self.client.get(url_for("get_city")

        self.assert200(response)
        self.assertIn(response.data.decode(), city)