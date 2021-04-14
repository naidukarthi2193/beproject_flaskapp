from flask import Flask, request, jsonify, Blueprint, make_response
from firebase_admin import credentials, firestore, initialize_app
from flaskapp.models import StudentProfile, TeacherProfile
from flaskapp.response import (
    OperationFailed,
    InternalServerError,
    NotFound,
    DataAlreadyExsist,
    OperationCorrect,
    MethodNotAvailable,
    AuthenticationFailed
)

cred = credentials.Certificate('./firebase.json')
default_app = initialize_app(cred)
db = firestore.client()

userManagementBlueprint = Blueprint("userManagementBlueprint", __name__)


@userManagementBlueprint.route('/', methods=["GET"])
def index():
    return "<h1>Welcome to our server !!</h1>"


@userManagementBlueprint.route('/login', methods=['GET', 'POST'])
def login_user():
    body = request.get_json(silent=True)
    if request.method == "POST":
        try:
            user_ref = db.collection('signupusers').document(body["email"])
            user_ref.set(body)
            profile_ref = db.collection('profile').document(body["email"])
            profile_ref.set(body)
            response = OperationCorrect(data=body)
        except Exception as e:
            response = OperationFailed(str(e))
    elif request.method == "GET":
        try:
            user_ref = db.collection('signupusers').document(body["email"])
            user = user_ref.get()
            if user.exists:
                user = user.to_dict()
                if body["email"] == user["email"] and body["password"] == user["password"]:
                    response = OperationCorrect(data=user)
                else:
                    response = AuthenticationFailed()
            else:
                response = NotFound()
        except Exception as e:
            response = OperationFailed(str(e))
    else:
        response = MethodNotAvailable()
    return response


@userManagementBlueprint.route('/profile', methods=['POST', 'GET'])
def profile_user():
    body = request.get_json(silent=True)
    try:
        user_ref = db.collection('profile').document(body["email"])
        user = user_ref.get()
        if user.exists:
            user = user.to_dict()
            if user["role"] == "student":
                user_obj = StudentProfile(**user)
            if user["role"] == "teacher":
                user_obj = TeacherProfile(**user)
            if request.method == "POST":
                try:
                    user_ref = db.collection('profile').document(body["email"])
                    modified_data = dict(user_obj.__dict__, **body)
                    user_ref.update(modified_data)
                    return OperationCorrect(data=modified_data)
                except Exception as e:
                    return OperationFailed(str(e))
            response = OperationCorrect(data=user)
        else:
            response = NotFound()
    except Exception as e:
        response = OperationFailed(str(e))
    return response
