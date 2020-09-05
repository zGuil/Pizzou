from flask_jwt import JWT, jwt_required, current_identity
from werkzeug.security import safe_str_cmp
from models.users import Users
from flask import Flask

users = Users.get_users()


username_table = {u.username: u for u in users}
userid_table = {u.id: u for u in users}


def authenticate(username, password):
    user = username_table.get(username, None)
    if user and safe_str_cmp(user.password.encode('utf-8'), password.encode('utf-8')):
        return user


def identity(payload):
    user_id = payload['identity']
    return userid_table.get(user_id, None)


app = Flask(__name__)
app.config['SECRET_KEY'] = 'super-secret'

jwt = JWT(app, authenticate, identity)


if __name__ == '__main__':
    app.run(debug=True)
