import json
import pdb

from application.models import Partner
from tests import utils

class TestPartnerResource():
    url_partner = '/api/v1/partner'
    url_partner_item = '/api/v1/partner/{}'
    url_nearest = '/api/v1/partner/nearest'

    def test_create_partner_endpoint(self, test_client, session, teardown):
        def should_create_a_partner(test_client, session):
            data = {
                'document': '00.000.000/0000-00',
                'email': 'danilolmoura@gmail.com',
                'name': 'Danilo da Silva'
            }

            res = test_client.post(
                self.url_partner,
                data=json.dumps(data),
                headers=utils.get_headers())

            assert res.status_code == 200
            res_json = json.loads(res.data)

            assert res_json['document'] == data['document']
            assert res_json['email'] == data['email']
            assert res_json['name'] == data['name']

        def should_raise_409_when_tries_to_creeate_a_partner_with_existing_document(test_client, session):
            data = {
                'document': '00.000.000/0000-01',
                'email': 'danilolmoura2@gmail.com',
                'name': 'Danilo da Silva'
            }

            res = test_client.post(
                self.url_partner,
                data=json.dumps(data),
                headers=utils.get_headers())

            assert res.status_code == 200

            # Change email and name but keep same document
            data['email'] = 'danilolmoura3@gmail.com'
            data['name'] = 'Danilo 3'

            res = test_client.post(
                self.url_partner,
                data=json.dumps(data),
                headers=utils.get_headers())

            assert res.status_code == 409

        def should_raise_409_when_tries_to_creeate_a_partner_with_existing_email(test_client, session):
            data = {
                'document': '00.000.000/00002',
                'email': 'danilolmoura3@gmail.com',
                'name': 'Danilo da Silva'
            }

            res = test_client.post(
                self.url_partner,
                data=json.dumps(data),
                headers=utils.get_headers())

            assert res.status_code == 200

            # Change email and name but keep same email
            data['document'] = '00.000.000/00002'
            data['name'] = 'Danilo 3'

            res = test_client.post(
                self.url_partner,
                data=json.dumps(data),
                headers=utils.get_headers())

            assert res.status_code == 409

        should_create_a_partner(test_client, session)
        should_raise_409_when_tries_to_creeate_a_partner_with_existing_document(test_client, session)
        should_raise_409_when_tries_to_creeate_a_partner_with_existing_email(test_client, session)

    def test_get_partner_endpoint(self, test_client, session, teardown):
        def should_return_partner_for_a_specified_id(test_client, session):
            data = {
                'document': '00.000.000/0000-10',
                'email': 'danilolmoura10@gmail.com',
                'name': 'Danilo da Silva'
            }

            # Create a partner
            res = test_client.post(
                self.url_partner,
                headers=utils.get_headers(),
                data=json.dumps(data))

            assert res.status_code == 200
            partner_id = json.loads(res.data)['$id']

            # get partner by id
            res = test_client.get(
                self.url_partner_item.format(partner_id),
                headers=utils.get_headers())

            partner_res = json.loads(res.data)

            assert len(partner_res.keys()) == 4
            assert partner_res['$id'] == partner_id
            assert partner_res['document'] == data['document']
            assert partner_res['email'] == data['email']
            assert partner_res['name'] == data['name']

        should_return_partner_for_a_specified_id(test_client, session)
