from elk.app import create_app
from elk.config import HTTP_PORT, DEBUG
from werkzeug.contrib.fixers import ProxyFix

#: WSGI endpoint
app = create_app()
app.wsgi_app = ProxyFix(app.wsgi_app)

if __name__ == '__main__':
    app.debug = DEBUG
    app.run(host='0.0.0.0', port=HTTP_PORT)
