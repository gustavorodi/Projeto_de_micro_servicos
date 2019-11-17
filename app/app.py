from flask import Flask, render_template, url_for, request, redirect, jsonify
from Helper.ConstantesParametro import ConstantesParametro
from Helper.Validate import Validate
import requests

app = Flask(__name__)

eventos = [
        {"nome": "Evento 1", "endereco":"Rua ...." , "descricao": "descricao","data": "21/11/2019" ,"horario": "10:00"},
        {"nome": "Evento 2", "endereco":"Rua ...." , "descricao": "descricao","data": "21/11/2019" ,"horario": "10:00"},
        {"nome": "Evento 2", "endereco":"Rua ...." , "descricao": "descricao","data": "21/11/2019" ,"horario": "10:00"},
    ]

@app.route("/")
def index():

    
    return render_template('index.html', nomeSite="Eventoss", data=eventos)

@app.route("/formulario-evento")
def formulario_evento():
    return render_template('/cadastro-eventos/formulario.html')

@app.route('/autenticar', methods=['POST', 'GET'])
def autenticar():

    if request.method == 'GET':
        return render_template('404.html')
    else:
        if Validate.empty(request.form[ConstantesParametro.email]):
            if Validate.empty(request.form[ConstantesParametro.senha]):

                email = request.form[ConstantesParametro.email]
                password = request.form[ConstantesParametro.senha]

                if 'mestra' == password:
                    return redirect(url_for('index'))

            else:
                #flash("Coloque senha")
                print('Sem senha')
                print(request.form[ConstantesParametro.senha])
        else:
            #flash("Coloque o email")
            print('Sem email')
            print(request.form[ConstantesParametro.email])

        return redirect('/login')

@app.route("/registrar")
def registrar():
    return render_template('registrar.html')

@app.route("/usuarioIndex")
def usuarioIndex():
    return render_template('usuarioIndex.html')

@app.route("/cadastrar-evento", methods=['POST'])
def cadastrar_evento():
    print('cadastrar_evento')
    nome = request.form[ConstantesParametro.nome]
    data = request.form[ConstantesParametro.data]
    horario = request.form[ConstantesParametro.horario]
    descricao = request.form[ConstantesParametro.descricao]
    rua = request.form[ConstantesParametro.rua]
    numero = request.form[ConstantesParametro.numero]
    cidade = request.form[ConstantesParametro.cidade]

    print(nome) 
    print(data) 
    print(horario) 
    print(descricao)
    print(rua)
    print(numero)
    print(cidade)   
    return redirect(url_for('index'))
    
@app.route("/cadastrar-contato", methods=['POST'])
def cadastrar_contato():
    cadastroName = request.form[ConstantesParametro.nome]
    cadastroEmail = request.form[ConstantesParametro.email]

    cadastro = {
                    'email': cadastroEmail,
                    'nome' : cadastroName
                }


    #localhost:8080
    x = requests.post('http://localhost:3000/person',data=cadastro)

    print(x.text)
    return x.text

@app.errorhandler(404)
def page_not_found(error):
   return render_template('404.html')

app.run(debug=True)
