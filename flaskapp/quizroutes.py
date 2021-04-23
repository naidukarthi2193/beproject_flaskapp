from flask import Flask, request, jsonify, Blueprint, make_response
from firebase_admin import credentials, firestore, initialize_app
from google.cloud.firestore import ArrayUnion
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
            if quiz_ref.get().exists:
                return DataAlreadyExsist()
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
            if quiz_arr:
                return OperationCorrect(data=quiz_arr)
            else:
                return NotFound()
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


@quizManagementBlueprint.route('/attemptQuiz', methods=['POST'])
def attempt_quiz_management():
    body = request.get_json(silent=True)
    if request.method == "POST":
        try:
            if body["quiz_id"] and body["correct_option"] and body["email"]:
                quiz_ref = db.collection('quiz').document(body["quiz_id"])
                quiz_data = quiz_ref.get()
                if quiz_data.exists:
                    quiz_data = quiz_data.to_dict()
                    if body["correct_option"] == quiz_data["correct_option"]:
                        try:
                            if body["email"] in quiz_data["quiz_data"]:
                                return DataAlreadyExsist()
                            else:
                                quiz_ref.update(
                                    {u'quiz_data': ArrayUnion([body["email"]])})
                                return OperationCorrect(data=body)
                        except Exception as e:
                            return OperationFailed(str(e))
                    else:
                        return NotFound(message="wrong answer")
                else:
                    return NotFound(message="quiz does not exist")
            else:
                return AuthenticationFailed()
        except Exception as e:
            return OperationCorrect(data=body)
