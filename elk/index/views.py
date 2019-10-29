from flask import Blueprint
from flask import render_template

bp = Blueprint('index', __name__)

@bp.route('/')
def api():
    return render_template('index.html')
