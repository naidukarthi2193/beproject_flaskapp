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
    AuthenticationFailed,
    DeleteSucessful
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
            if body:
                if "subject_id" in body:
                    subject_ref = db.collection('subject').where(
                        u'subject_id', u'==', body["subject_id"]).stream()
                if "email" in body:
                    subject_ref = db.collection('subject').where(
                        u'email', u'==', body["email"]).stream()
            else:
                subject_ref = db.collection('subject').stream()
            subject_arr = list()
            for subject in subject_ref:
                subject_arr.append(subject.to_dict())
            if subject_arr:
                return OperationCorrect(data=subject_arr)
            else:
                return NotFound()
        except Exception as e:
            return OperationFailed(str(e))


@lecturerManagementBlueprint.route('/lecture', methods=['GET', 'POST', 'DELETE'])
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
            if body:
                if "subject_id" in body:
                    lecture_ref = db.collection('lecture').where(
                        u'subject_id', u'==', body["subject_id"]).stream()
                if "lecture_id" in body:
                    lecture_ref = db.collection('lecture').where(
                        u'lecture_id', u'==', body["lecture_id"]).stream()
            else:
                lecture_ref = db.collection('lecture').stream()
            lecture_arr = list()
            for lecture in lecture_ref:
                lecture_arr.append(lecture.to_dict())
            if lecture_arr:
                return OperationCorrect(data=lecture_arr)
            else:
                return NotFound()
        except Exception as e:
            return OperationFailed(str(e))

    if request.method == "DELETE":
        try:
            if body:
                lecture = Lecture(**body)
                lecture_ref = db.collection('lecture').document(
                    str(lecture.lecture_day+lecture.lecture_time))
                if lecture_ref.get().exists:
                    lecture_ref.delete()
                    return DeleteSucessful()
                else:
                    return NotFound()
            else:
                return NotFound()
        except Exception as e:
            return OperationFailed(str(e))
