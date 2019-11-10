from flask import Blueprint
from flask import request
from flask import render_template
from flask_login import login_required
from .controller import Log


bp = Blueprint('loginfo', __name__)

@bp.route('/loginfo/search')
@login_required
def loginfo_search():
    data = Log.find_by_condition()
    return render_template('/loginfo/search.html', data=data)

@bp.route('/loginfo/search/logdisplay_sub', methods=['POST'])
@login_required
def logdisplay_sub():
    uid = request.form['uid']
    return render_template('/loginfo/search_logdisplay_sub.html', data=uid)
