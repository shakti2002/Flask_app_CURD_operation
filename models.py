from app import mongo, ma

class User:
    def __init__(self, id, name, email, password):
        self.id = id
        self.name = name
        self.email = email
        self.password = password

class UserSchema(ma.Schema):
    class Meta:
        fields = ('id', 'name', 'email', 'password')
