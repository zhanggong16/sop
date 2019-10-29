from flask import Blueprint
from flask import render_template
from elk.api.views import api_router

bp = Blueprint('index', __name__)

@bp.route('/api')
def api():
    return render_template('index.html', api_router=api_router)
