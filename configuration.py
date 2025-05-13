from routes.login import login_route
from routes.register import register_route
from routes.principal import principal_route
from routes.meu_pet import meu_pet_route
from routes.consultas import consultas_route
from routes.exames import exames_route
from routes.historico import historico_route
from routes.vacinas import vacinas_route

def configure_all(app):
    configure_routes(app)


def configure_routes(app):
    app.register_blueprint(login_route)
    app.register_blueprint(register_route)
    app.register_blueprint(principal_route)
    app.register_blueprint(meu_pet_route)
    app.register_blueprint(consultas_route)
    app.register_blueprint(exames_route)
    app.register_blueprint(historico_route)
    app.register_blueprint(vacinas_route)
