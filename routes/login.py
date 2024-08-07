from flask import Blueprint, render_template

login_route = Blueprint('login', __name__)

@login_route.route('/')
def login():
    """tela de login"""
    return render_template('login.html')