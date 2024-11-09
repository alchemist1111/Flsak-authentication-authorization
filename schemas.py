from marshmallow import Schema, fields, ValidationError  # type: ignore

class UserSchema(Schema):
    id = fields.Int()
    username = fields.Str(required=True)
    email = fields.Email(required=True)