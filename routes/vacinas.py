from flask import Blueprint, render_template

vacinas_route = Blueprint('vacinas', __name__)

@vacinas_route.route('/vacinas', methods=['GET','POST'])
def vacinas():
    """tela de vacinas"""
    return render_template('vacinas.html')