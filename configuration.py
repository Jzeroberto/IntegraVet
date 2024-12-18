from routes.login import login_route
from routes.register import register_route
<<<<<<< HEAD
from routes.principal import principal_route
=======
from routes.menu import menu_route

>>>>>>> 942379f1048953a96ed35a7f0ba8aabb203fcce1

def configure_all(app):
    configure_routes(app)


def configure_routes(app):
    app.register_blueprint(login_route)
    app.register_blueprint(register_route)
<<<<<<< HEAD
    app.register_blueprint(principal_route)
=======
    app.register_blueprint(menu_route)
>>>>>>> 942379f1048953a96ed35a7f0ba8aabb203fcce1
