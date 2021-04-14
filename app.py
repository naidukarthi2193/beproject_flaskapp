from flask import Flask, request, jsonify, Blueprint
from flaskapp.userroutes import userManagementBlueprint
from flaskapp.lectureroutes import lecturerManagementBlueprint
from firebase_admin import credentials, firestore, initialize_app


app = Flask(__name__)


app.register_blueprint(userManagementBlueprint)
app.register_blueprint(lecturerManagementBlueprint)

if __name__ == '__main__':
    app.run(threaded=True, port=5000, debug=True)
