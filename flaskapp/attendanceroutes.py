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
attendanceManagementBlueprint = Blueprint(
    "attendanceManagementBlueprint", __name__)


@attendanceManagementBlueprint.route('/attendLecture', methods=['POST'])
def attend_lecture():
    body = request.get_json(silent=True)
    try:
        attendance_ref = db.collection(
            'attendance').document(body["lecture_id"])
        lec_attendance = attendance_ref.get()
        if lec_attendance.exists:
            students = lec_attendance.to_dict()["students"]
            print(students)
            if body["email"] in students:
                return DataAlreadyExsist()
            else:
                attendance_ref.update(
                    {u'students': ArrayUnion([body["email"]])})
                attendance_ref.update({"total": Increment(1)})
                return OperationCorrect(data=body)
        else:
            return NotFound()
    except Exception as e:
        return OperationFailed(str(e))
