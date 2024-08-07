from routes.login import login_route


def configure_all(app):
    configure_routes(app)

def configure_routes(app):
    app.register_blueprint(login_route)