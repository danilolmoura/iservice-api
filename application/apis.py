import pdb

from flask_potion import fields, ModelResource
from flask_potion.routes import Route

from application.models import User, Product, Store

class UserResource(ModelResource):
    class Meta:
        include_id = True
        model = User
        name = 'user'

class StoreResource(ModelResource):
    class Meta:
        include_id = True
        model = Store
        name = 'store'

    class Schema:
        user = fields.ToOne('user')
        location = fields.Custom(
            {},
            converter=Store.location_from_json,
            formatter=Store.location_to_json)

        coverage_area = fields.Custom(
            {},
            converter=Store.coverage_area_from_json,
            formatter=Store.coverage_area_to_json)


class ProductResource(ModelResource):
    class Meta:
        include_id = True
        model = Product
        name = 'product'

def create_apis(api):
    api.add_resource(UserResource)
    api.add_resource(StoreResource)
    api.add_resource(ProductResource)
