#-*- coding:utf-8 -*-
from __future__ import with_statement

from flask import Flask, jsonify


class TestCase(object):
    def setUp(self):
        self.app = self.create_app()
        self.client = self.app.test_client()

    def create_app(self):
        from flask_request_params import get_request_params
        app = Flask(__name__)
        app.secret_key = 'secret'

        @app.route('/', methods=['POST'])
        def index():
            params = get_request_params()
            return jsonify(params)

        return app