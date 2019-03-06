from flask import Flask
from flask_restful import Api
from flask_migrate import Migrate

from utilities.ma import ma
from utilities.db import db
from utilities.jwt_settings import jwt_callbacks

from resources.user import *


app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql://Leo:p{:N38vuy&yLA**e@localhost:5432/AdlerLing"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["PROPAGATE_EXCEPTIONS"] = True
app.config["SQLALCHEMY_ECHO"] = True
app.config["JWT_BLACKLIST_ENABLED"] = True
app.config["JWT_BLACKLIST_TOKEN_CHECKS"] = [
    "access",
    "refresh"
]

app.secret_key = "shitty"  # TO DO: CHANGE THIS
api = Api(app)
jwt_callbacks(app)
migrate = Migrate(app, db)

api.add_resource(UserLogin, '/login')
api.add_resource(UserLogout, '/logout')
api.add_resource(UserRegister, '/register')
api.add_resource(User, '/user/<int:user_id>')
api.add_resource(UserCheck, '/check')
api.add_resource(AdminCheck, '/admin')


if __name__ == "__main__":
    db.init_app(app)
    ma.__init__(app)
    app.run(port=5000, debug=True)
