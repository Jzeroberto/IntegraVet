from flask import Blueprint, render_template

menu_route = Blueprint('menu', __name__)

@menu_route.route('/menu', methods=['POST'])
def menu():
    """tela principal"""
    return render_template('menu.html')