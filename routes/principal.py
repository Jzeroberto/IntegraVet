from flask import Blueprint, render_template

principal_route = Blueprint('principal', __name__)

servicos = [
    {"nome": "Consultas", "imagem": "static/images/consultas.jpeg", "rota": "consultas.consultas"},
    {"nome": "Exames", "imagem": "static/images/exames.jpeg", "rota": "exames.exames"},
    {"nome": "Vacinas", "imagem": "static/images/vacina.jpeg", "rota": "vacinas.vacinas"},
    {"nome": "Histórico Médico", "imagem": "static/images/historico.jpeg", "rota": "historico.historico"}
]



@principal_route.route('/principal', methods=['GET','POST'])
def principal():
    
    return render_template('principal.html', servicos=servicos)
    