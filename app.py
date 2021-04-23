from flask import Flask, request, jsonify, Blueprint, url_for
from flaskapp.userroutes import userManagementBlueprint
from flaskapp.lectureroutes import lecturerManagementBlueprint
from flaskapp.quizroutes import quizManagementBlueprint
from firebase_admin import credentials, firestore, initialize_app
import urllib
from flaskapp.response import (
    OperationCorrect
)

app = Flask(__name__)

app.register_blueprint(userManagementBlueprint)
app.register_blueprint(lecturerManagementBlueprint)
app.register_blueprint(quizManagementBlueprint)


def has_no_empty_params(rule):
    defaults = rule.defaults if rule.defaults is not None else ()
    arguments = rule.arguments if rule.arguments is not None else ()
    return len(defaults) >= len(arguments)


@app.route("/")
def site_map():
    output = []
    for rule in app.url_map.iter_rules():
        options = {}
        for arg in rule.arguments:
            options[arg] = "[{0}]".format(arg)
        methods = ','.join(rule.methods)
        url = url_for(rule.endpoint, **options)
        url_data = dict()
        url_data["functions"] = rule.endpoint
        url_data["methods"] = methods
        url_data["url"] = url
        output.append(url_data)
    return OperationCorrect(data=output)


if __name__ == '__main__':
    app.run(threaded=True, port=5000, debug=True)
