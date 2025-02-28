from flask import Blueprint, render_template

principal_route = Blueprint('principal', __name__)

@principal_route.route('/principal', methods=['POST'])
def principal():
    """tela principal"""
    return render_template('principal.html')