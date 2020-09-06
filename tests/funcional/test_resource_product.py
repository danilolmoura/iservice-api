import json
import pdb

from application.models import Product
from tests import utils

class TestProductResource():
    url_product = '/api/v1/product'
    url_product_item = '/api/v1/product/{}'
    url_change_status = '/api/v1/product/{}/status'
    url_request_exchange = '/api/v1/product/{}/exchange'
    url_find = '/api/v1/product/find'

    def test_create_product_endpoint(self, test_client, session, teardown):
        def should_create_a_product(test_client, session):
            pass

        should_create_a_product(test_client, session)

    def test_get_product_endpoint(self, test_client, session, teardown):
        def should_return_product_for_a_specified_id(test_client, session):
            pass

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
