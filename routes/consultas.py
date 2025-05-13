from flask import Blueprint, render_template

consultas_route = Blueprint('consultas', __name__)

@consultas_route.route('/consultas', methods=['GET','POST'])
def consultas():
    """tela de consultas"""
    return render_template('consultas.html')