from flask import Flask, request, jsonify, Blueprint, make_response
from firebase_admin import credentials, firestore, initialize_app
from flaskapp.models import QuizData
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
quizManagementBlueprint = Blueprint(
    "quizManagementBlueprint", __name__)


@quizManagementBlueprint.route('/quizData', methods=['GET', 'POST', 'DELETE'])
def quiz_data_management():
    body = request.get_json(silent=True)
    if request.method == "POST":
        try:

            quiz_ref = db.collection('quiz').document(body["quiz_id"])
            quiz_ref.set(QuizData(**body).__dict__)
            return OperationCorrect(data=body)
        except Exception as e:
            return OperationFailed(str(e))
    if request.method == "GET":
        try:
            if body:
                if "lecture_id" in body:
                    quiz_ref = db.collection('quiz').where(
                        u'lecture_id', u'==', body["lecture_id"]).stream()
                if "quiz_id" in body:
                    quiz_ref = db.collection('quiz').where(
                        u'quiz_id', u'==', body["quiz_id"]).stream()
            else:
                quiz_ref = db.collection('quiz').stream()
            quiz_arr = list()
            for quiz in quiz_ref:
                quiz_arr.append(quiz.to_dict())
            return OperationCorrect(data=quiz_arr)
        except Exception as e:
            return OperationFailed(str(e))

    if request.method == "DELETE":
        try:
            if body:
                quiz = QuizData(**body)
                quiz_ref = db.collection('quiz').document(quiz.quiz_id)
                if quiz_ref.get().exists:
                    quiz_ref.delete()
                    return DeleteSucessful()
                else:
                    return NotFound()
            else:
                return NotFound()
        except Exception as e:
            return OperationFailed(str(e))
