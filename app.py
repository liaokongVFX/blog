# -*- coding: utf-8 -*-
# Time    : 2019/4/24 22:34
# Author  : LiaoKong


from flask import Flask

from settings import config

from blueprints.auth import auth_bp

from extensions import db


def create_app(config_name=None):
    if config_name is None:
        config_name = "development"

    app = Flask(__name__)
    app.config.from_object(config[config_name])

    register_blueprints(app)
    register_extensions(app)
    register_logging(app)
    register_shell_context(app)
    register_template_context(app)
    register_errors(app)
    register_command(app)
    register_request_handlers(app)

    return app


def register_logging(app):
    pass


def register_extensions(app):
    db.init_app(app)


def register_blueprints(app):
    app.register_blueprint(auth_bp, url_prefix="/auth")


def register_shell_context(app):
    pass


def register_template_context(app):
    pass


def register_errors(app):
    pass


def register_command(app):
    pass


def register_request_handlers(app):
    pass


if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)
