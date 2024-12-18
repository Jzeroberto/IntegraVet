from routes.login import login_route
from routes.register import register_route
from routes.principal import principal_route

def configure_all(app):
    configure_routes(app)


def configure_routes(app):
    app.register_blueprint(login_route)
    app.register_blueprint(register_route)
    app.register_blueprint(principal_route)