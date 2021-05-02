from flask import Flask, request, jsonify, Blueprint, make_response
from firebase_admin import credentials, firestore, initialize_app
from flaskapp.models import Subject, Lecture
from google.cloud.firestore import ArrayUnion, Increment
from collections import Counter
import os
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
from twilio.jwt.access_token import AccessToken
from twilio.jwt.access_token.grants import VideoGrant

db = firestore.client()
twilioBlueprint = Blueprint(
    "twilioBlueprint", __name__)
twilio_account_sid = os.environ.get('TWILIO_ACCOUNT_SID')
twilio_api_key_sid = os.environ.get('TWILIO_API_KEY_SID')
twilio_api_key_secret = os.environ.get('TWILIO_API_KEY_SECRET')


@twilioBlueprint.route('/twiliologin', methods=['POST'])
def teacherLecture():
    body = request.get_json(force=True)
    email = body.get('email')
    lecture_id = body.get('lecture_id')
    if not email:
        return AuthenticationFailed()
    token = AccessToken(twilio_account_sid, twilio_api_key_sid,
                        twilio_api_key_secret, identity=email)
    token.add_grant(VideoGrant(room=lecture_id))
    return {'token': token.to_jwt().decode()}
