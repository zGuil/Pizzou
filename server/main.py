from flask import Flask
from flask_cors import CORS
from flask_jwt import JWT, jwt_required, current_identity
from werkzeug.security import safe_str_cmp

from routes.users import bp as bp_users
from routes.produto import bp as bp_produtos
from controllers.users import authenticate, identity
from __init__ import app


CORS(app)
app.config['SECRET_KEY'] = 'super-secret'
jwt = JWT(app, authenticate, identity)

app.register_blueprint(bp_users)
app.register_blueprint(bp_produtos)
