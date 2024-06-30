import unittest
from flask import json
from Monitoring_system import app, db
from Monitoring_system.models import Webserver, Request


class WebserverTestCase(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        db.create_all()

        self.webserver_data = {
            'name': 'Test Server',
            'url': 'http://example.com'
        }

    def tearDown(self):
        db.session.remove()
        db.drop_all()

    def test_create_webserver(self):
        response = self.app.post('/webservers', data=json.dumps(self.webserver_data), content_type='application/json')
        self.assertEqual(response.status_code, 201)
        self.assertIn('Webserver created', response.get_data(as_text=True))


if __name__ == '__main__':
    unittest.main()
