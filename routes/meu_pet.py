from flask import Blueprint, render_template

meu_pet_route = Blueprint('meu_pet', __name__)

pets = [
    
        {'nome': 'Max', 'foto': 'aa', 'raça': 'Labrador', 'idade': 6, 'status': 'Saudável'},
        {'nome': 'Bella', 'foto': 'aa', 'raça': 'Poodle', 'idade': 4, 'status': 'Alergia Alimentar'}
]


@meu_pet_route.route('/meu_pet', methods=['GET','POST'])
def meu_pet():
    """tela de meu pet"""
    return render_template('meu_pet.html', pets=pets)