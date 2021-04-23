from flask import Flask, request, jsonify, Blueprint, url_for, send_from_directory
from flaskapp.userroutes import userManagementBlueprint
from flaskapp.lectureroutes import lecturerManagementBlueprint
from flaskapp.quizroutes import quizManagementBlueprint
from flaskapp.attendanceroutes import attendanceManagementBlueprint
from flaskapp.reportroutes import reportManagementBlueprint
from firebase_admin import credentials, firestore, initialize_app
import urllib
import os
from flaskapp.response import (
    OperationCorrect
)

app = Flask(__name__)


@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'),
                               'favicon.ico', mimetype='image/vnd.microsoft.icon')


app.register_blueprint(userManagementBlueprint)
app.register_blueprint(lecturerManagementBlueprint)
app.register_blueprint(quizManagementBlueprint)
app.register_blueprint(attendanceManagementBlueprint)
app.register_blueprint(reportManagementBlueprint)


@app.route("/")
def site_map():
    output = []
    for rule in app.url_map.iter_rules():
        options = {}
        for arg in rule.arguments:
            options[arg] = "[{0}]".format(arg)
        methods = rule.methods
        methods.discard("OPTIONS")
        methods.discard("HEAD")
        methods = ','.join(methods)
        url = url_for(rule.endpoint, **options)
        url_data = dict()
        url_data["functions"] = rule.endpoint
        url_data["methods"] = methods
        url_data["url"] = url
        output.append(url_data)
    return OperationCorrect(data=output)


if __name__ == '__main__':
    app.run(threaded=True, port=5000, debug=True)
