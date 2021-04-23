from flask import Flask, request, jsonify, Blueprint, make_response
from firebase_admin import credentials, firestore, initialize_app
from flaskapp.models import Subject, Lecture
from google.cloud.firestore import ArrayUnion, Increment
from collections import Counter
from flaskapp.response import (
    OperationFailed,
    InternalServerError,
    NotFound,
    DataAlreadyExsist,
    OperationCorrect,
    MethodNotAvailable,
    AuthenticationFailed,
    DeleteSucessful
)
db = firestore.client()
reportManagementBlueprint = Blueprint(
    "reportManagementBlueprint", __name__)


@reportManagementBlueprint.route('/teacherLecture', methods=['POST'])
def teacherLecture():
    body = request.get_json(silent=True)
    return NotFount()
