from email import message
from flask import Flask, jsonify, request
from app.exception.email_already_exists import EmailAlreadyExistsError
from app.exception.wrong_type import WrongType
from app.models.user_model import User

app = Flask(__name__)


@app.get("/user")
def get_user():
    return jsonify(User.get_users()), 200


@app.post("/user")
def create_new_user():
    try:
        new_user = User(**request.get_json())
        return new_user.create_user(), 201

    except EmailAlreadyExistsError as e:
        return {"message": e.message}, e.code

    except WrongType as e:
        return {
            "wrong fields":
                {
                    e.type_request: e.wrong
                }
        }, e.code
