# -*- coding: utf-8 -*-
from flask import abort, Blueprint, current_app, Flask, jsonify, redirect, \
    request
from flask_dance.contrib.github import make_github_blueprint, github
from flask_login import login_required
from sqlalchemy.orm.exc import NoResultFound

__all__ = ["view", "github_view"]

view = Blueprint("auth", __name__)
github_view = make_github_blueprint()


@view.route('')
@login_required
def index():
    return "", 200
