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

    name = db.Column(
        db.String(128),
        nullable=False,
        doc='nome do parceiro')

    email = db.Column(
        db.String(128),
        nullable=False,
        unique=True,
        doc='email')

    document = db.Column(
        db.String(128),
        nullable=False,
        unique=True,
        doc='cpf ou cnpj')

    store_id = db.Column(
        db.Integer,
        db.ForeignKey('store.id'),
        nullable=False,
        unique=True,
        doc='id da loja')

    store = db.relationship('Store')


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

    owner = db.relationship(
        'Partner',
        back_populates="store",
        primaryjoin="Partner.store_id==Store.id")


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
