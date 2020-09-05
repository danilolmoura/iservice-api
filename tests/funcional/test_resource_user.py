import json
import pdb

from application.models import User
from tests import utils

class TestUserResource():
    url_user = '/api/v1/user'
    url_user_item = '/api/v1/user/{}'
    url_nearest = '/api/v1/user/nearest'

    def test_create_user_endpoint(self, test_client, session, teardown):
        def should_create_a_user(test_client, session):
            data = {
                'document': '00.000.000/0000-00',
                'email': 'danilolmoura@gmail.com',
                'name': 'Danilo da Silva',
                'password': '12345'
            }

            res = test_client.post(
                self.url_user,
                data=json.dumps(data),
                headers=utils.get_headers())

            assert res.status_code == 200
            res_json = json.loads(res.data)

            assert res_json['document'] == data['document']
            assert res_json['email'] == data['email']
            assert res_json['name'] == data['name']

        def should_raise_409_when_tries_to_creeate_a_user_with_existing_document(test_client, session):
            data = {
                'document': '00.000.000/0000-01',
                'email': 'danilolmoura2@gmail.com',
                'name': 'Danilo da Silva',
                'password': '12345'
            }

            res = test_client.post(
                self.url_user,
                data=json.dumps(data),
                headers=utils.get_headers())

            assert res.status_code == 200

            # Change email and name but keep same document
            data['email'] = 'danilolmoura3@gmail.com'
            data['name'] = 'Danilo 3'

            res = test_client.post(
                self.url_user,
                data=json.dumps(data),
                headers=utils.get_headers())

            assert res.status_code == 409

        def should_raise_409_when_tries_to_creeate_a_user_with_existing_email(test_client, session):
            data = {
                'document': '00.000.000/00002',
                'email': 'danilolmoura3@gmail.com',
                'name': 'Danilo da Silva',
                'password': '12345'
            }

            res = test_client.post(
                self.url_user,
                data=json.dumps(data),
                headers=utils.get_headers())

            assert res.status_code == 200

            # Change email and name but keep same email
            data['document'] = '00.000.000/00002'
            data['name'] = 'Danilo 3'

            res = test_client.post(
                self.url_user,
                data=json.dumps(data),
                headers=utils.get_headers())

            assert res.status_code == 409

        should_create_a_user(test_client, session)
        should_raise_409_when_tries_to_creeate_a_user_with_existing_document(test_client, session)
        should_raise_409_when_tries_to_creeate_a_user_with_existing_email(test_client, session)

    def test_get_user_endpoint(self, test_client, session, teardown):
        def should_return_user_for_a_specified_id(test_client, session):
            data = {
                'document': '00.000.000/0000-10',
                'email': 'danilolmoura10@gmail.com',
                'name': 'Danilo da Silva',
                'password': '12345'
            }

            # Create a user
            res = test_client.post(
                self.url_user,
                headers=utils.get_headers(),
                data=json.dumps(data))

            assert res.status_code == 200
            user_id = json.loads(res.data)['$id']

            # get user by id
            res = test_client.get(
                self.url_user_item.format(user_id),
                headers=utils.get_headers())

            user_res = json.loads(res.data)

            assert len(user_res.keys()) == 5
            assert user_res['$id'] == user_id
            assert user_res['document'] == data['document']
            assert user_res['email'] == data['email']
            assert user_res['name'] == data['name']
            assert user_res['password'] == data['password']

        should_return_user_for_a_specified_id(test_client, session)
