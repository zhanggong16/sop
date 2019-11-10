from flask import Blueprint
from flask import request
from flask import render_template
from flask_login import login_required
from .controller import Database

bp = Blueprint('system', __name__)

@bp.route('/system/database')
@login_required
def system_database():
    database_all_list = Database.all_list()
    first_data = Database.format_data(database_all_list[0])
    return render_template('/system/database.html', data=database_all_list,
                                                    first_data=first_data)

@bp.route('/system/database/detail_table_sub', methods=['POST'])
@login_required
def detail_table_sub():
    uid = request.form['uid']
    detail = Database.detail_data(uid)
    return render_template('/system/database_detail_table_sub.html', first_data=detail)
