from flask import Blueprint
from flask import request, jsonify
from flask import render_template
from flask_login import login_required
from .controller import HostMonitor, Performance

bp = Blueprint('performance', __name__)

@bp.route('/performance/host')
@login_required
def host():
    all_list = HostMonitor.host_all_list()
    return render_template('/performance/host.html', data=all_list)

@bp.route('/performance/host/<hostname>', methods=['GET', 'POST'])
@login_required
def performance_host(hostname):
    title_list = HostMonitor.get_title_list()
    return render_template('/performance/host_monitor_display.html', hostname=hostname,
                                        title_data=title_list)

@bp.route('/performance/host/json_data', methods=['GET', 'POST'])
@login_required
def json_data():
    if request.method == 'POST':
        starttime = request.form['start']
        endtime = request.form['end']
        hostname = request.form['hostname']
        data_list = HostMonitor.get_monitor_json_data(hostname, starttime, endtime)
    return jsonify({'data': data_list})

@bp.route('/performance/index/<opt>')
@login_required
def index(opt):
    wait_class_data = Performance.wait_class(opt)
    return render_template('/performance/index.html', wait_class_data=wait_class_data)
