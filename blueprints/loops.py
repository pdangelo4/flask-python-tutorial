
from flask import Blueprint, render_template, request, redirect

loops_blueprint = Blueprint('loops', __name__, url_prefix='/loops')

@loops_blueprint.route('/')
def index():
       return render_template('loops/index.html')
   