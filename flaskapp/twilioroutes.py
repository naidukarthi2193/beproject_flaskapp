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
import numpy as np
from twilio.jwt.access_token import AccessToken
from twilio.jwt.access_token.grants import VideoGrant

db = firestore.client()
twilioBlueprint = Blueprint(
    "twilioBlueprint", __name__)
twilio_account_sid = os.environ.get(
    'TWILIO_ACCOUNT_SID', "AC26d2cdf7ef7a49dee692b7c5d8cc52f4")
twilio_api_key_sid = os.environ.get(
    'TWILIO_API_KEY_SID', "SK67e22e0438e9998a0ee91f18ed0d3c1e")
twilio_api_key_secret = os.environ.get(
    'TWILIO_API_KEY_SECRET', "xdIX2ajCaPDSlVzK9HHE2Dv76djHnmIh")


db = firestore.client()


def tolerant_mean(arrs):
    lens = [len(i) for i in arrs]
    arr = np.ma.empty((np.max(lens), len(arrs)))
    arr.mask = True
    for idx, l in enumerate(arrs):
        arr[:len(l), idx] = l
    return arr.mean(axis=-1), arr.std(axis=-1)


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


@twilioBlueprint.route('/classAttention', methods=['POST'])
def classAttention():
    body = request.get_json(force=True)
    try:
        attention_ref = db.collection(
            'attention').document(body["lecture_id"]).get()
        attentiondata = attention_ref.to_dict()
        grapharr = []
        for key in attentiondata.keys():
            grapharr.append([data["attention"] for data in attentiondata[key]])
        # print(grapharr)
        grapharr = np.array(grapharr, dtype=object)
        classAvg, error = tolerant_mean(grapharr)
    except Exception as e:
        print(e)
        return OperationFailed()
    return OperationCorrect(data=classAvg.tolist(0))
