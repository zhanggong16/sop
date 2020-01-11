from flask import Flask
from flask import Response
from flask_restful import Api
from flask_apscheduler import APScheduler
from werkzeug.utils import import_string
from werkzeug.datastructures import Headers


blueprints = [
    'elk.error.views:bp',
    'elk.index.views:bp',
    'elk.monkey.views:bp',
    'elk.system.views:bp',
    'elk.loginfo.views:bp',
    'elk.auth.views:bp',
    'elk.performance.views:bp'
]

extensions = [
    'elk.extension:login_manager'
]

api_router = import_string('elk.api.views:api_router')

def create_app(config=None):
    app = Flask(__name__)
    app.config.from_object('elk.scheduled_task.scheduler')
    app.secret_key = 'sop secret key'
    app.response_class = CorsResponse
    api = Api(app, catch_all_404s=True)
    
    #define blueprint
    for blueprint_name in blueprints:
        blueprint = import_string(blueprint_name)
        app.register_blueprint(blueprint)
 
    #define extension
    for ext_name in extensions:
        extension = import_string(ext_name)
        extension.init_app(app)

    #register api
    for router in api_router:
        api.add_resource(router['resource_name'], router['url'])
       
    scheduler = APScheduler()
    scheduler.init_app(app)
    scheduler.start()

    return app


class CorsResponse(Response):

    def __init__(self, response=None, **kwargs):
        kwargs['headers'] = ''
        headers = kwargs.get('headers')

        origin = ('Access-Control-Allow-Origin', '*')
        methods = ('Access-Control-Allow-Headers', 'Content-Type')
        if headers:
            headers.add(*origin)
            headers.add(*methods)
        else:
            headers = Headers([origin, methods])
        kwargs['headers'] = headers
        return super(CorsResponse, self).__init__(response, **kwargs)
