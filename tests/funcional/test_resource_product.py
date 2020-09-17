import json
import pdb

from application.models import Product, Store, User
from tests import utils

class TestProductResource():
    url_product = '/api/v1/product'
    url_store = '/api/v1/store'
    url_product_item = '/api/v1/product/{}'
    url_change_status = '/api/v1/product/{}/status'
    url_request_exchange = '/api/v1/product/{}/exchange'
    url_find = '/api/v1/product/find'

    def test_create_product_endpoint(self, test_client, session, teardown):
        def should_create_a_product(test_client, session):
            user = utils.create_user(
                session,
                **{
                    'document': '00.000.000/0000-00',
                    'email': 'danilolmoura@gmail.com',
                    'name': 'Danilo da Silva',
                    'password': '12345'
                }
            )

            store_data = {
                'name': 'Loja do Danilo',
                'coverage_area': Store.coverage_area_from_json([
                        [
                            [-22.885576, -43.276030],
                            [-22.904009, -43.297860],
                            [-22.910643, -43.271918]
                        ]
                    ]),
                    'location': Store.location_from_json({
                            'lat': -22.894507,
                            'lng': -43.260745
                    }),
                    'user_id': user.id
            }

            store = utils.create_store(session, **store_data)

            data_product = {
                'category': 1,
                'description': 'Bola de vôlei 2 anos de uso',
                'image_urls': ['https://cdn.ecvol.com/s/www.querocase.com.br/produtos/topsocket-bola-de-volei/z/0.png'],
                'is_active': True,
                'is_for_exchange': True,
                'is_for_sale': False,
                'name': 'Bola de vôlei',
                'store': store.id,
            }

            res = test_client.post(
                self.url_product,
                data=json.dumps(data_product),
                headers=utils.get_headers())

            assert res.status_code == 200

            product_json = json.loads(res.data)
            assert data_product['category'] == product_json['category']
            assert data_product['description'] == product_json['description']
            assert data_product['image_urls'] == product_json['image_urls']
            assert data_product['is_active'] == product_json['is_active']
            assert data_product['is_for_exchange'] == product_json['is_for_exchange']
            assert data_product['is_for_sale'] == product_json['is_for_sale']
            assert data_product['name'] == product_json['name']

        should_create_a_product(test_client, session)

    def test_get_product_endpoint(self, test_client, session, teardown):
        def should_return_product_for_a_specified_id(test_client, session):
            user = utils.create_user(
                session,
                User,
                **{
                    'document': '00.000.000/0000-00',
                    'email': 'danilolmoura@gmail.com',
                    'name': 'Danilo da Silva',
                    'password': '12345'
                }
            )

            store_data = {
                "name": "Loja do Danilo",
                "coverage_area": [
                        [
                            [-22.885576, -43.276030],
                            [-22.904009, -43.297860],
                            [-22.910643, -43.271918]
                        ]
                    ],
                    "location": {
                            "lat": -22.894507,
                            "lng": -43.260745
                    },
                    "user": user.id
            }

            res = test_client.post(
                self.url_store,
                data=json.dumps(store_data),
                headers=utils.get_headers())

            assert res.status_code == 200
            store = json.loads(res.data)

            data_product = {
                'category': 1,
                'description': 'Bola de vôlei 2 anos de uso',
                'image_urls': ['https://cdn.ecvol.com/s/www.querocase.com.br/produtos/topsocket-bola-de-volei/z/0.png'],
                'is_active': True,
                'is_for_exchange': True,
                'is_for_sale': False,
                'name': 'Bola de vôlei',
                'store': store.get('$id'),
            }

            res = test_client.post(
                self.url_product,
                data=json.dumps(data_product),
                headers=utils.get_headers())

            assert res.status_code == 200

            product_json = json.loads(res.data)
            assert data_product['category'] == product_json['category']
            assert data_product['description'] == product_json['description']
            assert data_product['image_urls'] == product_json['image_urls']
            assert data_product['is_active'] == product_json['is_active']
            assert data_product['is_for_exchange'] == product_json['is_for_exchange']
            assert data_product['is_for_sale'] == product_json['is_for_sale']
            assert data_product['name'] == product_json['name']

        def should_return_only_specific_product_fields(test_client, session):
            pass

        should_return_product_for_a_specified_id(test_client, session)
        should_return_only_specific_product_fields(test_client, session)

    def test_find_products_endpoint(self, test_client, session, teardown):
        def should_return_products_fieltered_by_distance(test_client, session):
            pass

        def should_return_products_fieltered_by_category(test_client, session):
            pass

        def should_return_only_active_fields(test_client, session):
            pass

        def should_return_only_specific_product_fields(test_client, session):
            pass

        def should_return_an_empty_list_if_theres_no_product_in_range(test_client, session):
            pass

        should_return_products_fieltered_by_distance(test_client, session)
        should_return_products_fieltered_by_category(test_client, session)
        should_return_only_active_fields(test_client, session)
        should_return_only_specific_product_fields(test_client, session)
        should_return_an_empty_list_if_theres_no_product_in_range(test_client, session)

    def test_product_status(self, test_client, session, teardown):
        def should_set_status_as_active(test_client, session):
            pass

        def should_set_status_as_inactive(test_client, session):
            pass

        should_set_status_as_active(test_client, session)
        should_set_status_as_inactive(test_client, session)

    def test_request_exchange(self, test_client, session, teardown):
        def should_return_400_when_tries_to_give_inactive_product(test_client, session):
            pass

        def should_return_400_when_tries_to_recieve_inactive_product(test_client, session):
            pass

        should_return_400_when_tries_to_give_inactive_product(test_client, session)
        should_return_400_when_tries_to_recieve_inactive_product(test_client, session)
