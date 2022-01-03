from flask import Blueprint, request, jsonify, render_template
import jwt
from functools import wraps
from werkzeug.security import generate_password_hash, check_password_hash
from ..database.database import db, Users, user_schemas, user_schema
from ..config.config import producction
import logging


# encode_jwt = jwt.encode({"user": "jose"}, "secret", algorithm="HS256")
#decode_jwt = jwt.decode(encode_jwt,"secret", algorithms="HS256")

app_bp = Blueprint("app_bp", __name__, url_prefix="/app/v1/")


def Token(f):
    @wraps(f)
    def wrapper():
        token = request.args.get("token")

        if token:
            validate = Users.query.filter_by(token=token).all()

            if validate:
                return f()

            else:
                return jsonify({"Error": "Token not valid"}), 400

        else:
            return jsonify({"Error": "Token not provided"}), 400

    return wrapper


class Methods:

    def Signup(self,):
        info = request.json

        validate_email = Users.query.filter_by(
            email=info["email"]).first()

        if validate_email:

            return jsonify("This email already exist"), 404

        else:
            secret = producction.SECRET_KEY

            hash_password = generate_password_hash(
                info["password"], method="sha256")

            token = jwt.encode(
                {"name": info["name"], "pass": hash_password}, secret, algorithm="HS256")

            user = Users(info['name'], info['email'], hash_password, token)
            db.session.add(user)
            db.session.commit()

            return jsonify({"Status": "Account succefully created"}), 200

    def Login(self,):
        info = request.json

        if info["email"] and info["password"]:
            user = Users.query.filter_by(email=info["email"]).first()
            unhashed_password = check_password_hash(
                user.password, info['password'])

            if unhashed_password:
                return jsonify({"Token": user.token})

            else:
                return jsonify({"Error": "Data incorrect"}), 400

        else:
            return jsonify({"Error": "User or Password not provided"}), 400

    def User_List(self,):
        result = Users.query.all()
        users = user_schemas.dump(result)
        return jsonify(users), 200

    def User_Update(self,):
        token = request.args.get("token")
        info = request.json

        result = Users.query.filter_by(token=token).first()

        new_password = generate_password_hash(
            info["password"], method="sha256")

        secret = producction.SECRET_KEY

        new_token = jwt.encode(
            {"name": info["name"], "password": new_password}, secret, algorithm="HS256")

        result.name = info["name"]
        result.email = info["email"]
        result.password = new_password
        result.token = new_token

        db.session.commit()

        return jsonify({"Status": "Update Sucessfully", "New_token": new_token}), 200


@app_bp.route("/signup", methods=['POST'])
def Signup():
    caller = Methods()
    return caller.Signup()


@app_bp.route("/login", methods=['GET'])
def Login():
    caller = Methods()
    return caller.Login()


# @app_bp.route("/logout", methods=['GET'])
# def Logout():

#     return "logout"


@app_bp.route("/user", methods=['GET', 'PATCH'])
@Token
def User():
    caller = Methods()
    if request.method == 'GET':
        return caller.User_List()

    elif request.method == 'PATCH':
        return caller.User_Update()
