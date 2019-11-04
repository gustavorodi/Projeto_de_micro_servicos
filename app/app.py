from flask import Flask, render_template, url_for, request, redirect
from app.Helper.ConstantesParametro import ConstantesParametro
from app.Helper.Validate import Validate

app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/login")
def login():
    return render_template('login.html')

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

@app.errorhandler(404)
def page_not_found(error):
   return render_template('404.html')

app.run(debug=True)