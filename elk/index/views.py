from flask import Blueprint
from flask import render_template
from flask_login import login_required


bp = Blueprint('index', __name__)

@bp.route('/index')
@login_required
def index():
    return render_template('index.html')
