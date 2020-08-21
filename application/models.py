from flask_sqlalchemy import SQLAlchemy
from geoalchemy2 import Geometry

db = SQLAlchemy()

class Partner(db.Model):
    """Define schema for partner table
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

    name = db.Column(
        db.String(128),
        nullable=False,
        doc='nome do parceiro')

    store = db.relationship(
        'Store',
        back_populates="partner",
        primaryjoin="Store.partner_id==Partner.id")

    def to_json(self):
        pass


class Store(db.Model):
    """Define schema for store table
    """

    id = db.Column(
        db.Integer,
        primary_key=True,
        doc='id da loja')

    name = db.Column(
        db.String(128),
        nullable=False,
        doc='nome da loja')

    location = db.Column(
        Geometry(geometry_type='POINT'),
        nullable=False,
        index=True,
        doc='Localização da loja')

    coverage_area = db.Column(
        Geometry(geometry_type='MULTIPOLYGON'),
        nullable=False,
        index=True,
        doc='Area de cobertura da loja')

    partner_id = db.Column(
        db.Integer,
        db.ForeignKey('partner.id'),
        nullable=False,
        unique=True,
        doc='id da parceiro')

    partner = db.relationship('Partner')

    @staticmethod
    def location_from_json(data):
        return True

    @staticmethod
    def location_to_json(data):
        return True

    @staticmethod
    def coverage_area_from_json(data):
        return True

    @staticmethod
    def coverage_area_to_json(data):
        return True

    def to_json(self):
        pass

class Product(db.Model):
    """Define schema for product table
    """

    id = db.Column(
        db.Integer,
        primary_key=True,
        doc='id da loja')

    name = db.Column(
        db.String(128),
        nullable=False,
        doc='nome da loja')

    description = db.Column(
        db.String(512),
        nullable=False,
        doc='descrição do produto')

    category = db.Column(
        db.Integer,
        nullable=False,
        doc='categoria do produto')

    def to_json(self):
        pass
