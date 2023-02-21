from marshmallow import Schema, fields

from app.setup_db import db


class Genre(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)


class GenreSchema(Schema):
    id = fields.Integer(dump_only=True)
    name = fields.String()
