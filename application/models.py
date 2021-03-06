from flask_sqlalchemy import SQLAlchemy
from geoalchemy2 import Geometry
from geoalchemy2.shape import from_shape, to_shape
from shapely.geometry import Point, Polygon, MultiPolygon

db = SQLAlchemy()

class User(db.Model):
    """Define schema for user table
    """

    id = db.Column(
        db.Integer,
        primary_key=True,
        doc='id do parceiro')

    document = db.Column(
        db.String(128),
        nullable=False,
        unique=True,
        doc='cpf ou cnpj')

    email = db.Column(
        db.String(128),
        nullable=False,
        unique=True,
        doc='email')

    password = db.Column(
        db.String(24),
        nullable=False,
        unique=False,
        doc='password')

    name = db.Column(
        db.String(128),
        nullable=False,
        doc='nome do parceiro')

    store = db.relationship(
        'Store',
        back_populates="user",
        primaryjoin="Store.user_id==User.id")

    def to_json(self):
        pass


class Store(db.Model):
    """Define schema for store table
    """

    id = db.Column(
        db.Integer,
        primary_key=True,
        doc='id da loja')

    coverage_area = db.Column(
        Geometry(geometry_type='MULTIPOLYGON'),
        nullable=False,
        index=True,
        doc='Area de cobertura da loja')

    location = db.Column(
        Geometry(geometry_type='POINT'),
        nullable=False,
        index=True,
        doc='Localização da loja')

    name = db.Column(
        db.String(128),
        nullable=False,
        doc='nome da loja')

    user_id = db.Column(
        db.Integer,
        db.ForeignKey('user.id'),
        nullable=False,
        unique=True,
        doc='id da parceiro')

    user = db.relationship('User')

    products = db.relationship(
        'Product',
        back_populates="store",
        primaryjoin="Product.store_id==Store.id")

    @staticmethod
    def location_from_json(data):
        wkb_element = from_shape(Point(data['lat'], data['lng']))

        return wkb_element

    @staticmethod
    def location_to_json(data):
        point = to_shape(data)

        return {
            'lat': point.x,
            'lng': point.y
        }

    @staticmethod
    def coverage_area_from_json(data):
        polygons = [Polygon(polygon) for polygon in data]

        wkb_element = from_shape(MultiPolygon(polygons))

        return wkb_element

    @staticmethod
    def coverage_area_to_json(data):
        multipolygon = to_shape(data)

        return [polygon.exterior.coords[:-1] for polygon in multipolygon]

    def to_json(self):
        pass


class Product(db.Model):
    """Define schema for product table
    """

    id = db.Column(
        db.Integer,
        primary_key=True,
        doc='id da loja')

    category = db.Column(
        db.Integer,
        nullable=False,
        doc='categoria do produto')

    description = db.Column(
        db.String(512),
        nullable=False,
        doc='descrição do produto')

    image_urls = db.Column(
        db.ARRAY(db.String(512)),
        nullable=False,
        doc='lista de imagens do produto')

    is_active = db.Column(
        db.Boolean,
        nullable=False,
        default=True,
        doc='está ativo')

    is_for_exchange = db.Column(
        db.Boolean,
        nullable=False,
        default=True,
        doc='disponível para troca')

    is_for_sale = db.Column(
        db.Boolean,
        nullable=False,
        default=False,
        doc='disponível para venda')

    name = db.Column(
        db.String(128),
        nullable=False,
        doc='nome da loja')

    store_id = db.Column(
        db.Integer,
        db.ForeignKey('store.id'),
        nullable=False,
        unique=True,
        doc='id da loja')

    store = db.relationship('Store')

    def to_json(self):
        return {
            'id': self.id,
            'category': self.category,
            'description': self.description,
            'image_urls': self.image_urls,
            'is_active': self.is_active,
            'is_for_exchange': self.is_for_exchange,
            'is_for_sale': self.is_for_sale,
            'name': self.name,
            'store_id': self.store_id,
        }

    @staticmethod
    def image_urls_from_json(data):
        return data

    @staticmethod
    def image_urls_to_json(data):
        return data

