# -*- coding: UTF-8 -*-
from flask import Blueprint, render_template, redirect, request, url_for
from flask_login import login_user, logout_user, login_required
from .manager import do_auth, User
import sys

bp = Blueprint('auth', __name__)

@bp.route('/', methods=['GET', 'POST'])
def login():
    reload(sys)
    sys.setdefaultencoding('utf-8')
    login_res = '请输入用户名、密码。'
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        try:
            remember = request.form['remember']
        except Exception:
            remember = 0
        auth_res = do_auth(username, password)
        if auth_res:
            uid, role = auth_res
            user = User(username, uid, role)
            login_user(user, remember)
            return redirect(request.args.get("next") or url_for('index.index'))
        else:
            login_res = '输入的用户名、密码不正确，请重新输入。'
    return render_template('auth/login.html', login_res=login_res)


@bp.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('auth.login'))
