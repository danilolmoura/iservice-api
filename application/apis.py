import pdb

from flask_potion import fields, ModelResource
from flask_potion.routes import Route
from geoalchemy2.shape import from_shape, to_shape
from shapely.geometry import Point

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

    class Schema:
        store = fields.ToOne('store')
        image_urls = fields.Custom(
            {},
            converter=Product.image_urls_from_json,
            formatter=Product.image_urls_to_json)

    @Route.GET('/nearest')
    def nearest(
        self,
        lat: fields.Number(nullable=False),
        lng: fields.Number(nullable=False),
        distance: fields.Integer(nullable=False, default=2)):
        """Find nearest Products given an specific position
            and max distance (in km)

        Args:
            lat  (Number): latitude of the given position
            long (Number): longitude of the given position
            distance (Integer): max distance between the given point and Store

        Returns:
            list(dict): List of representation of products found
        """

        point = Point(lat, lng)

        stores = Store.query.all()
        products = []
        for store in stores:
            location = to_shape(store.location)

            if location.distance(point) <= distance:
                products.extend(
                    [
                        product.to_json()
                        for product in store.products
                        if product.is_active
                    ]
                )

        return products

def create_apis(api):
    api.add_resource(UserResource)
    api.add_resource(StoreResource)
    api.add_resource(ProductResource)
