import pdb

from flask_potion import fields, ModelResource
from flask_potion.routes import Route
from geoalchemy2.shape import from_shape, to_shape
from shapely.geometry import Point

from application.models import Partner, Product, Store

class PartnerResource(ModelResource):
    class Meta:
        include_id = True
        model = Partner
        name = 'partner'


class StoreResource(ModelResource):
    class Meta:
        include_id = True
        model = Store
        name = 'store'


class ProductResource(ModelResource):
    class Meta:
        include_id = True
        model = Product
        name = 'product'

def create_apis(api):
    api.add_resource(PartnerResource)
    api.add_resource(StoreResource)
    api.add_resource(ProductResource)
