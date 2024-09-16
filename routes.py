from flask import request, jsonify
from app import app, mongo
from app.models import UserSchema

user_schema = UserSchema()
users_schema = UserSchema(many=True)

@app.route('/users', methods=['GET'])
def get_users():
    users = mongo.db.users.find()
    return jsonify(users_schema.dump(users))

@app.route('/users/<id>', methods=['GET'])
def get_user(id):
    user = mongo.db.users.find_one_or_404({'id': id})
    return jsonify(user_schema.dump(user))

@app.route('/users', methods=['POST'])
def create_user():
    data = request.get_json()
    user = {
        'id': data['id'],
        'name': data['name'],
        'email': data['email'],
        'password': data['password']
    }
    mongo.db.users.insert_one(user)
    return jsonify(user_schema.dump(user)), 201

@app.route('/users/<id>', methods=['PUT'])
def update_user(id):
    data = request.get_json()
    mongo.db.users.update_one(
        {'id': id},
        {'$set': {
            'name': data['name'],
            'email': data['email'],
            'password': data['password']
        }}
    )
    user = mongo.db.users.find_one_or_404({'id': id})
    return jsonify(user_schema.dump(user))

@app.route('/users/<id>', methods=['DELETE'])
def delete_user(id):
    mongo.db.users.delete_one({'id': id})
    return jsonify({'message': 'User deleted successfully'})


