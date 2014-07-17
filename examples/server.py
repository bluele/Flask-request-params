#-*- coding:utf-8 -*-
from flask import Flask, request, render_template, jsonify
from flask_request_params import bind_request_params


app = Flask(__name__)
app.secret_key = 'secret'
# bind rails like params to request.params
app.before_request(bind_request_params)


class User(object):
    def __init__(self, name, password):
        self.name = name
        self.password = password

    def save(self):
        if not (self.name and self.password):
            raise ValueError()
        return True


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/user', methods=['POST'])
def create_user():
    params = request.params.require('user').permit('name', 'password')
    user = User(**params)
    user.save()
    return jsonify(params)


@app.route('/echo/<path>', methods=['GET', 'POST'])
def echo(path):
    return jsonify(request.params)

app.run(debug=True)
