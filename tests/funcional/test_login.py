import json
import pdb

from application.models import User
from tests import utils

class TestLogin():
    url_login = '/api/v1/login'
    url_user = '/api/v1/user'

    def test_login(self, test_client, session, teardown):
        def should_login_using_email_and_password(test_client, session):
            data = {
                'document': '00.000.000/0000-01',
                'email': 'danilolmoura@gmail.com',
                'name': 'Danilo da Silva',
                'password': '12345'
            }

            res = test_client.post(
                self.url_user,
                data=json.dumps(data),
                headers=utils.get_headers())

            assert res.status_code == 200
            
            login_data = {
                'email': data['email'],
                'password': data['password'],
            }
            res = test_client.post(
                self.url_login,
                data=json.dumps(login_data),
                headers=utils.get_headers())

            assert res.status_code == 200
            login_result = json.loads(res.data)
            assert 'access_token' in login_result

        should_login_using_email_and_password(test_client, session)
