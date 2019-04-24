# -*- coding: utf-8 -*-
# Time    : 2019/4/24 22:08
# Author  : LiaoKong

from flask import Blueprint

auth_bp = Blueprint("auth", __name__)


@auth_bp.route("/login/")
def login():
    pass


@auth_bp.route("/logout/")
def logout():
    pass


