# from flask_login import (
#     LoginManager,
#     login_user,
#     login_required,
#     logout_user,
#     current_user,
# )
from flask import Flask

# from flask import request, render_template, redirect, flash, url_for
import os

# import requests
# import json
# from requests.models import Response
# from unittest.mock import Mock
# from isodate import parse_duration


# from sqlalchemy.exc import IntegrityError
# from datetime import timedelta

from model import db


""" Begin boilerplate code """


def create_app():
    app = Flask(__name__, static_url_path="")
    app.config["SQLALCHEMY_DATABASE_URI"] = "db key"
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = True
    app.config["SECRET_KEY"] = "c3a93f55-2015-4042-9ef7-77de85976f78"
    db.init_app(app)
    return app


app = create_app()

app.app_context().push()


@app.route("/", methods=["GET", "POST"])
def main():
    return "success", 200


if __name__ == "__main__":
    # Bind to PORT if defined, otherwise default to 5000.
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=True)  # Remember to remove Debug
