from flask import jsonify
from utilities.blacklist import BLACKLIST
from flask_jwt_extended import JWTManager


def jwt_callbacks(app):
    jwt = JWTManager(app)

    @jwt.user_identity_loader
    def user_identity_lookup(user):
        return user

    @jwt.user_claims_loader
    def add_claims_to_access_token(user):
        claims = []
        [claims.append(x["name"]) for x in user["roles"]]
        return {'roles': claims}

    @jwt.token_in_blacklist_loader
    def check_if_token_in_blacklist(decrypted_token):
        return (
                decrypted_token["jti"] in BLACKLIST
        )

    @jwt.expired_token_loader
    def expired_token_callback():
        return jsonify(
            {
                "message": "The token has expired.",
                "error": "token_expired"
            }
        ), 401

    @jwt.invalid_token_loader
    def invalid_token_callback(error):
        return (
            jsonify(
                {
                    "message": "Signature verification failed.",
                    "error": "invalid_token"
                }
            ),
            401,
        )

    @jwt.unauthorized_loader
    def missing_token_callback(error):
        return (
            jsonify(
                {
                    "description": "Request does not contain an access token.",
                    "error": "authorization_required",
                }
            ),
            401,
        )

    @jwt.needs_fresh_token_loader
    def token_not_fresh_callback():
        return (
            jsonify(
                {
                    "description": "The token is not fresh.",
                    "error": "fresh_token_required"
                }
            ),
            401,
        )

    @jwt.revoked_token_loader
    def revoked_token_callback():
        return (
            jsonify(
                {
                    "description": "The token has been revoked.",
                    "error": "token_revoked"
                }
            ),
            401,
        )
