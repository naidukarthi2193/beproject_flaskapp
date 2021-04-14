from flask import Flask, request, jsonify, Blueprint, make_response
from firebase_admin import credentials, firestore, initialize_app
from flaskapp.models import Subject, Lecture
from flaskapp.response import (
    OperationFailed,
    InternalServerError,
    NotFound,
    DataAlreadyExsist,
    OperationCorrect,
    MethodNotAvailable,
    AuthenticationFailed
)
db = firestore.client()
lecturerManagementBlueprint = Blueprint(
    "lecturerManagementBlueprint", __name__)


@lecturerManagementBlueprint.route('/subjects', methods=['GET', 'POST'])
def subject_management():
    body = request.get_json(silent=True)
    if request.method == "POST":
        try:
            subject = Subject(**body)
            subject_ref = db.collection('subject').document(body["subject_id"])
            subject_ref.set(subject.__dict__)
            return OperationCorrect(data=body)
        except Exception as e:
            return OperationFailed(str(e))
    else:
        try:
            subject_ref = db.collection('subject').stream()
            subject_arr = list()
            for subject in subject_ref:
                subject_arr.append(subject.to_dict())
            return OperationCorrect(data=subject_arr)
        except Exception as e:
            return OperationFailed(str(e))


@lecturerManagementBlueprint.route('/lecture', methods=['GET', 'POST'])
def lecture_management():
    body = request.get_json(silent=True)
    if request.method == "POST":
        try:
            lecture = Lecture(**body)
            lecture_ref = db.collection('lecture').document(
                str(lecture.lecture_day+lecture.lecture_time))
            if lecture_ref.get().exists:
                return DataAlreadyExsist()
            else:
                lecture_ref.set(lecture.__dict__)
                return OperationCorrect(data=body)
        except Exception as e:
            return OperationFailed(str(e))
    if request.method == "GET":
        try:
            print(body)
            if body:
                if "subject_id" in body:
                    lecture_ref = db.collection('lecture').where(
                        u'subject_id', u'==', body["subject_id"]).stream()
                if "lecture_id" in body:
                    lecture_ref = db.collection('lecture').where(
                        u'lecture_id', u'==', body["lecture_id"]).stream()
            else:
                lecture_ref = db.collection('lecture').stream()
            print(lecture_ref)
            lecture_arr = list()
            for lecture in lecture_ref:
                lecture_arr.append(lecture.to_dict())
            return OperationCorrect(data=lecture_arr)
        except Exception as e:
            return OperationFailed(str(e))
