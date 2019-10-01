
from flask import Blueprint, redirect, render_template, request
from datetime import datetime

operators_blueprint = Blueprint('operators', __name__, url_prefix='/operators')

@operators_blueprint.route('/', methods=('GET', 'POST'))
def index():
    if request.method == 'GET':
        return render_template('operators/index.html')
    elif request.method == 'POST':
        # db.operators