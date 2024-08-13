from routes.login import login_route
from routes.register import register_route
from routes.menu import menu_route


def configure_all(app):
    configure_routes(app)


def configure_routes(app):
    app.register_blueprint(login_route)
    app.register_blueprint(register_route)
    app.register_blueprint(menu_route)