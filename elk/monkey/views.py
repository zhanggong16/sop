from flask import Blueprint
from flask import redirect, url_for

bp = Blueprint('monkey', __name__)

###js
@bp.route('/assets/global/plugins/jquery.min.js')
def jquery_min_js():
    return redirect(url_for('static', filename='assets/global/plugins/jquery.min.js'))

@bp.route('/assets/global/plugins/bootstrap/js/bootstrap.min.js')
def bootstrap_min_js():
    return redirect(url_for('static', filename='assets/global/plugins/bootstrap/js/bootstrap.min.js'))

@bp.route('/assets/global/plugins/js.cookie.min.js')
def js_cookie_min_js():
    return redirect(url_for('static', filename='assets/global/plugins/js.cookie.min.js'))

@bp.route('/assets/global/plugins/jquery-slimscroll/jquery.slimscroll.min.js')
def jquery_slimscroll_min_js():
    return redirect(url_for('static', filename='assets/global/plugins/jquery-slimscroll/jquery.slimscroll.min.js'))

@bp.route('/assets/global/plugins/jquery.blockui.min.js')
def jquery_blockui_min_js():
    return redirect(url_for('static', filename='assets/global/plugins/jquery.blockui.min.js'))

@bp.route('/assets/global/plugins/bootstrap-switch/js/bootstrap-switch.min.js')
def bootstrap_switch_min_js():
    return redirect(url_for('static', filename='assets/global/plugins/bootstrap-switch/js/bootstrap-switch.min.js'))

@bp.route('/assets/global/plugins/moment.min.js')
def moment_min_js():
    return redirect(url_for('static', filename='assets/global/plugins/moment.min.js'))

@bp.route('/assets/global/plugins/morris/morris.min.js')
def morris_min_js():
    return redirect(url_for('static', filename='assets/global/plugins/morris/morris.min.js'))

@bp.route('/assets/global/plugins/morris/raphael-min.js')
def raphael_min_js():
    return redirect(url_for('static', filename='assets/global/plugins/morris/raphael-min.js'))

@bp.route('/assets/global/plugins/counterup/jquery.waypoints.min.js')
def jquery_waypoints_min_js():
    return redirect(url_for('static', filename='assets/global/plugins/counterup/jquery.waypoints.min.js'))

@bp.route('/assets/global/plugins/counterup/jquery.counterup.min.js')
def jquery_counterup_min_js():
    return redirect(url_for('static', filename='assets/global/plugins/counterup/jquery.counterup.min.js'))

@bp.route('/assets/global/plugins/amcharts/amcharts/amcharts.js')
def amcharts_js():
    return redirect(url_for('static', filename='assets/global/plugins/amcharts/amcharts/amcharts.js'))

@bp.route('/assets/global/plugins/amcharts/amcharts/serial.js')
def serial_js():
    return redirect(url_for('static', filename='assets/global/plugins/amcharts/amcharts/serial.js'))

@bp.route('/assets/global/plugins/amcharts/amcharts/pie.js')
def pie_js():
    return redirect(url_for('static', filename='assets/global/plugins/amcharts/amcharts/pie.js'))

@bp.route('/assets/global/plugins/amcharts/amcharts/radar.js')
def radar_js():
    return redirect(url_for('static', filename='assets/global/plugins/amcharts/amcharts/radar.js'))

@bp.route('/assets/global/plugins/amcharts/amcharts/themes/light.js')
def light_js():
    return redirect(url_for('static', filename='assets/global/plugins/amcharts/amcharts/themes/light.js'))

@bp.route('/assets/global/plugins/amcharts/amcharts/themes/patterns.js')
def patterns_js():
    return redirect(url_for('static', filename='assets/global/plugins/amcharts/amcharts/themes/patterns.js'))

@bp.route('/assets/global/plugins/amcharts/amcharts/themes/chalk.js')
def chalk_js():
    return redirect(url_for('static', filename='assets/global/plugins/amcharts/amcharts/themes/chalk.js'))

@bp.route('/assets/global/plugins/amcharts/ammap/ammap.js')
def ammap_js():
    return redirect(url_for('static', filename='assets/global/plugins/amcharts/ammap/ammap.js'))

@bp.route('/assets/global/plugins/amcharts/ammap/maps/js/worldLow.js')
def worldlow_js():
    return redirect(url_for('static', filename='assets/global/plugins/amcharts/ammap/maps/js/worldLow.js'))

@bp.route('/assets/global/plugins/amcharts/amstockcharts/amstock.js')
def amstock_js():
    return redirect(url_for('static', filename='assets/global/plugins/amcharts/amstockcharts/amstock.js'))

@bp.route('/assets/global/plugins/fullcalendar/fullcalendar.min.js')
def fullcalendar_min_js():
    return redirect(url_for('static', filename='assets/global/plugins/fullcalendar/fullcalendar.min.js'))

@bp.route('/assets/global/plugins/horizontal-timeline/horizontal-timeline.js')
def horizontal_timeline_js():
    return redirect(url_for('static', filename='assets/global/plugins/horizontal-timeline/horizontal-timeline.js'))

@bp.route('/assets/global/plugins/flot/jquery.flot.min.js')
def jquery_flot_min_js():
    return redirect(url_for('static', filename='assets/global/plugins/flot/jquery.flot.min.js'))

@bp.route('/assets/global/plugins/flot/jquery.flot.resize.min.js')
def jquery_flot_resize_min_js():
    return redirect(url_for('static', filename='assets/global/plugins/flot/jquery.flot.resize.min.js'))

@bp.route('/assets/global/plugins/flot/jquery.flot.categories.min.js')
def jquery_flot_categories_min_js():
    return redirect(url_for('static', filename='assets/global/plugins/flot/jquery.flot.categories.min.js'))

@bp.route('/assets/global/plugins/jquery-easypiechart/jquery.easypiechart.min.js')
def jquery_easypiechart_min_js():
    return redirect(url_for('static', filename='assets/global/plugins/jquery-easypiechart/jquery.easypiechart.min.js'))

@bp.route('/assets/global/plugins/jquery.sparkline.min.js')
def jquery_sparkline_min_js():
    return redirect(url_for('static', filename='assets/global/plugins/jquery.sparkline.min.js'))

@bp.route('/assets/global/plugins/jqvmap/jqvmap/jquery.vmap.js')
def jquery_vmap_js():
    return redirect(url_for('static', filename='assets/global/plugins/jqvmap/jqvmap/jquery.vmap.js'))

@bp.route('/assets/global/plugins/jqvmap/jqvmap/maps/jquery.vmap.russia.js')
def jquery_vmap_russia_js():
    return redirect(url_for('static', filename='assets/global/plugins/jqvmap/jqvmap/maps/jquery.vmap.russia.js'))

@bp.route('/assets/global/plugins/jqvmap/jqvmap/maps/jquery.vmap.world.js')
def jquery_vmap_world_js():
    return redirect(url_for('static', filename='assets/global/plugins/jqvmap/jqvmap/maps/jquery.vmap.world.js'))

@bp.route('/assets/global/plugins/jqvmap/jqvmap/maps/jquery.vmap.europe.js')
def jquery_vmap_europe_js():
    return redirect(url_for('static', filename='assets/global/plugins/jqvmap/jqvmap/maps/jquery.vmap.europe.js'))

@bp.route('/assets/global/plugins/jqvmap/jqvmap/maps/jquery.vmap.germany.js')
def jquery_vmap_germany_js():
    return redirect(url_for('static', filename='assets/global/plugins/jqvmap/jqvmap/maps/jquery.vmap.germany.js'))

@bp.route('/assets/global/plugins/jqvmap/jqvmap/maps/jquery.vmap.usa.js')
def jquery_vmap_usa_js():
    return redirect(url_for('static', filename='assets/global/plugins/jqvmap/jqvmap/maps/jquery.vmap.usa.js'))

@bp.route('/assets/global/plugins/jqvmap/jqvmap/data/jquery.vmap.sampledata.js')
def jquery_vmap_sampledata_js():
    return redirect(url_for('static', filename='assets/global/plugins/jqvmap/jqvmap/data/jquery.vmap.sampledata.js'))

@bp.route('/assets/global/scripts/app.min.js')
def app_min_js():
    return redirect(url_for('static', filename='assets/global/scripts/app.min.js'))

@bp.route('/assets/pages/scripts/dashboard.min.js')
def dashboard_min_js():
    return redirect(url_for('static', filename='assets/pages/scripts/dashboard.min.js'))

@bp.route('/assets/layouts/layout/scripts/layout.min.js')
def layout_min_js():
    return redirect(url_for('static', filename='assets/layouts/layout/scripts/layout.min.js'))

@bp.route('/assets/layouts/layout/scripts/demo.min.js')
def demo_min_js():
    return redirect(url_for('static', filename='assets/layouts/layout/scripts/demo.min.js'))

@bp.route('/assets/layouts/global/scripts/quick-sidebar.min.js')
def quick_sidebar_min_js():
    return redirect(url_for('static', filename='assets/layouts/global/scripts/quick-sidebar.min.js'))

@bp.route('/assets/layouts/global/scripts/quick-nav.min.js')
def quick_nav_min_js():
    return redirect(url_for('static', filename='assets/layouts/global/scripts/quick-nav.min.js'))

@bp.route('/assets/global/scripts/datatable.js')
def datatable_js():
    return redirect(url_for('static', filename='assets/global/scripts/datatable.js'))

@bp.route('/assets/global/plugins/datatables/datatables.min.js')
def datatables_min_js():
    return redirect(url_for('static', filename='assets/global/plugins/datatables/datatables.min.js'))

@bp.route('/assets/global/plugins/datatables/plugins/bootstrap/datatables.bootstrap.js')
def datatables_bootstrap_js():
    return redirect(url_for('static', filename='assets/global/plugins/datatables/plugins/bootstrap/datatables.bootstrap.js'))

@bp.route('/assets/pages/scripts/table-datatables-colreorder.min.js')
def table_datatables_colreorder_min_js():
    return redirect(url_for('static', filename='assets/pages/scripts/table-datatables-colreorder.min.js'))

@bp.route('/assets/pages/scripts/table-datatables-managed.min.js')
def table_datatables_managed_min_js():
    return redirect(url_for('static', filename='assets/pages/scripts/table-datatables-managed.min.js'))

@bp.route('/assets/pages/scripts/table-datatables-buttons.min.js')
def table_datatables_buttons_min_js():
    return redirect(url_for('static', filename='assets/pages/scripts/table-datatables-buttons.min.js'))

@bp.route('/assets/global/plugins/bootstrap-daterangepicker/daterangepicker.min.js')
def daterangepicker_min_js():
    return redirect(url_for('static', filename='assets/global/plugins/bootstrap-daterangepicker/daterangepicker.min.js'))

@bp.route('/assets/global/plugins/bootstrap-growl/jquery.bootstrap-growl.min.js')
def jquery_bootstrap_growl_min_js():
    return redirect(url_for('static', filename='assets/global/plugins/bootstrap-growl/jquery.bootstrap-growl.min.js'))

@bp.route('/assets/highcharts/highcharts.js')
def highcharts_js():
    return redirect(url_for('static', filename='assets/highcharts/highcharts.js'))

@bp.route('/assets/highcharts/highcharts-3d.js')
def highcharts_3d_js():
    return redirect(url_for('static', filename='assets/highcharts/highcharts-3d.js'))

@bp.route('/assets/highcharts/heatmap.js')
def heatmap_js():
    return redirect(url_for('static', filename='assets/highcharts/heatmap.js'))

@bp.route('/assets/highcharts/organization.js')
def organization_js():
    return redirect(url_for('static', filename='assets/highcharts/organization.js'))

@bp.route('/assets/highcharts/networkgraph.js')
def networkgraph_js():
    return redirect(url_for('static', filename='assets/highcharts/networkgraph.js'))

@bp.route('/assets/highcharts/sankey.js')
def sankey_js():
    return redirect(url_for('static', filename='assets/highcharts/sankey.js'))

@bp.route('/assets/highcharts/data.js')
def data_js():
    return redirect(url_for('static', filename='assets/highcharts/data.js'))

@bp.route('/assets/highcharts/drilldown.js')
def drilldown_js():
    return redirect(url_for('static', filename='assets/highcharts/drilldown.js'))

@bp.route('/assets/highcharts/highcharts-more.js')
def highcharts_more_js():
    return redirect(url_for('static', filename='assets/highcharts/highcharts-more.js'))

@bp.route('/assets/highcharts/solid-gauge.js')
def solid_gauge():
    return redirect(url_for('static', filename='assets/highcharts/solid-gauge.js'))

@bp.route('/assets/pages/scripts/login.min.js')
def login_js():
    return redirect(url_for('static', filename='assets/pages/scripts/login.min.js'))

@bp.route('/assets/global/plugins/jquery-validation/js/jquery.validate.min.js')
def jquery_validate_min_js():
    return redirect(url_for('static', filename='assets/global/plugins/jquery-validation/js/jquery.validate.min.js'))

@bp.route('/assets/global/plugins/jquery-validation/js/additional-methods.min.js')
def additional_methods_min_js():
    return redirect(url_for('static', filename='assets/global/plugins/jquery-validation/js/additional-methods.min.js'))

@bp.route('/assets/global/plugins/select2/js/select2.full.min.js')
def select2_full_min_js():
    return redirect(url_for('static', filename='assets/global/plugins/select2/js/select2.full.min.js'))

@bp.route('/assets/global/plugins/backstretch/jquery.backstretch.min.js')
def jquery_backstretch_min_js():
    return redirect(url_for('static', filename='assets/global/plugins/backstretch/jquery.backstretch.min.js'))

@bp.route('/assets/global/plugins/bootstrap-multiselect/js/bootstrap-multiselect.js')
def bootstrap_multiselect_js():
    return redirect(url_for('static', filename='assets/global/plugins/bootstrap-multiselect/js/bootstrap-multiselect.js'))

@bp.route('/assets/pages/scripts/components-bootstrap-multiselect.min.js')
def components_bootstrap_mulitselect_min_js():
    return redirect(url_for('static', filename='assets/pages/scripts/components-bootstrap-multiselect.min.js'))


###css
@bp.route('/assets/global/plugins/font-awesome/css/font-awesome.min.css')
def font_awesome_min_css():
    return redirect(url_for('static', filename='assets/global/plugins/font-awesome/css/font-awesome.min.css'))

@bp.route('/assets/global/plugins/simple-line-icons/simple-line-icons.min.css')
def simple_line_icons_min_css():
    return redirect(url_for('static', filename='assets/global/plugins/simple-line-icons/simple-line-icons.min.css'))

@bp.route('/assets/global/plugins/bootstrap/css/bootstrap.min.css')
def bootstrap_min_css():
    return redirect(url_for('static', filename='assets/global/plugins/bootstrap/css/bootstrap.min.css'))

@bp.route('/assets/global/plugins/bootstrap-switch/css/bootstrap-switch.min.css')
def bootstrap_switch_min_css():
    return redirect(url_for('static', filename='assets/global/plugins/bootstrap-switch/css/bootstrap-switch.min.css'))

@bp.route('/assets/global/plugins/bootstrap-daterangepicker/daterangepicker.min.css')
def daterangepicker_min_css():
    return redirect(url_for('static', filename='assets/global/plugins/bootstrap-daterangepicker/daterangepicker.min.css'))

@bp.route('/assets/global/plugins/morris/morris.css')
def morris_css():
    return redirect(url_for('static', filename='assets/global/plugins/morris/morris.css'))

@bp.route('/assets/global/plugins/fullcalendar/fullcalendar.min.css')
def fullcalendar_min_css():
    return redirect(url_for('static', filename='assets/global/plugins/fullcalendar/fullcalendar.min.css'))

@bp.route('/assets/global/plugins/jqvmap/jqvmap/jqvmap.css')
def jqvmap():
    return redirect(url_for('static', filename='assets/global/plugins/jqvmap/jqvmap/jqvmap.css'))

@bp.route('/assets/global/css/components.min.css')
def components_min_css():
    return redirect(url_for('static', filename='assets/global/css/components.min.css'))

@bp.route('/assets/global/css/plugins.min.css')
def plugins_min_css():
    return redirect(url_for('static', filename='assets/global/css/plugins.min.css'))

@bp.route('/assets/layouts/layout/css/layout.min.css')
def layout_min_css():
    return redirect(url_for('static', filename='assets/layouts/layout/css/layout.min.css'))

@bp.route('/assets/layouts/layout/css/themes/blue.min.css')
def default_min_css():
    return redirect(url_for('static', filename='assets/layouts/layout/css/themes/blue.min.css'))

@bp.route('/assets/layouts/layout/css/custom.min.css')
def custom_min_css():
    return redirect(url_for('static', filename='assets/layouts/layout/css/custom.min.css'))

@bp.route('/assets/global/css/googleapis.css')
def googleapis_css():
    return redirect(url_for('static', filename='assets/global/css/googleapis.css'))

@bp.route('/assets/global/plugins/datatables/datatables.min.css')
def datatales_min_css():
    return redirect(url_for('static', filename='assets/global/plugins/datatables/datatables.min.css'))

@bp.route('/assets/global/plugins/datatables/plugins/bootstrap/datatables.bootstrap.css')
def datatables_bootstrap_css():
    return redirect(url_for('static', filename='assets/global/plugins/datatables/plugins/bootstrap/datatables.bootstrap.css'))

@bp.route('/assets/pages/css/login.min.css')
def login_css():
    return redirect(url_for('static', filename='assets/pages/css/login.min.css'))

@bp.route('/assets/global/plugins/select2/css/select2.min.css')
def select2_min_css():
    return redirect(url_for('static', filename='assets/global/plugins/select2/css/select2.min.css'))

@bp.route('/assets/global/plugins/select2/css/select2-bootstrap.min.css')
def select2_bootstrap_min_css():
    return redirect(url_for('static', filename='assets/global/plugins/select2/css/select2-bootstrap.min.css'))

@bp.route('/assets/global/plugins/bootstrap-multiselect/css/bootstrap-multiselect.css')
def bootstrip_mulitselect_css():
    return redirect(url_for('static', filename='assets/global/plugins/bootstrap-multiselect/css/bootstrap-multiselect.css'))


### img
@bp.route('/assets/layouts/layout/img/logodsm.png')
def logodsm_png():
    return redirect(url_for('static', filename='assets/layouts/layout/img/logodsm.png'))

@bp.route('/monitor/assets/layouts/layout/img/logodsm.png')
def monitor_logodsm_png():
    return redirect(url_for('static', filename='assets/layouts/layout/img/logodsm.png'))

@bp.route('/assets/layouts/layout/img/top_server.png')
def top_server_png():
    return redirect(url_for('static', filename='assets/layouts/layout/img/top_server.png'))

