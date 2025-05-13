from flask import Blueprint, render_template

historico_route = Blueprint('historico', __name__)

@historico_route.route('/historico', methods=['GET','POST'])
def historico():
    """tela de historico"""
    return render_template('historico.html')