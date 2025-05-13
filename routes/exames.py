from flask import Blueprint, render_template

exames_route = Blueprint('exames', __name__)

@exames_route.route('/exames', methods=['GET','POST'])
def exames():
    """tela de exames"""
    return render_template('exames.html')