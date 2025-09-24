#Importamos la libreria matplotlib que nos ayuda a graficas
from flask import Flask, render_template, request, redirect, session, flash
#hash para la encriptacion de la cadena de bloques
import hashlib
#Se guarda en una base de datos mongodb
from pymongo import MongoClient
from pymongo import ASCENDING, DESCENDING
import pymongo

from flask_bootstrap import Bootstrap



from flask import Flask, render_template_string
import dash
from dash import html, dcc
import plotly.express as px
import pandas as pd

from argon2 import PasswordHasher
from datetime import datetime


# Crear app Flask
app = Flask(__name__)

# Crear app Dash embebida en Flask
dash_app = dash.Dash(
    __name__,
    server=app
)

app.secret_key = b'\xaa\xe4V}y~\x84G\xb5\x95\xa0\xe0\x96\xca\xa7\xe7'


# Crear una instancia del encriptador Argon2
ph = PasswordHasher(
    time_cost=3,       # N° de iteraciones (mayor = más lento y seguro)
    memory_cost=65536, # Memoria en KiB (64 MiB)
    parallelism=4,     # Número de hilos (depende de CPU)
    hash_len=32,       # Tamaño del hash
    salt_len=16        # Tamaño del salt
    )



# Formulario para iniciar sesión


@app.route("/login")
def login():
    return render_template("login.html")

@app.route("/")
def raiz_login():
    return render_template('login.html')

@app.route("/Escritorio")
def escritorio():
    return render_template("Escritorio.html")

# Cerrar sesión
@app.route("/logout")
def logout():
    session.pop("usuario", None)
    return redirect("/login.html")




# Manejar login
@app.route("/hacer_login", methods=["POST"])
def hacer_login():
    AL_49695_Var = request.form["AL_49695_Var"]
    AL_79917_Var = request.form["AL_79917_Var"]
    # Aquí comparamos. Lo hago así de fácil por simplicidad
    # En la vida real debería ser con una base de datos y una contraseña hasheada
    if AL_49695_Var == "prueba@mail.com" and AL_79917_Var == "123":
        # Si coincide, iniciamos sesión y además reAL_63624_Varamos
        session["usuario"] = AL_49695_Var
        # Aquí puedes colocar más datos. Por ejemplo
        # session["nivel"] = "administrador"
        return redirect("/Escritorio")
    else:
        # Si NO coincide, lo regresamos
        flash("AL_49695_Var o contraseña incorrectos")
        return redirect("/login")


# Un "middleware" que se ejecuta antes de responder a cualquier AL_81549_Var. Aquí verificamos si el usuario ha iniciado sesión
@app.before_request
def antes_de_cada_peticion():
    AL_81549_Var = request.path
    # Si no ha iniciado sesión y no quiere ir a algo relacionado al login, lo reAL_63624_Varamos al login
    if not 'usuario' in session and AL_81549_Var != "/login" and AL_81549_Var != "/hacer_login" and AL_81549_Var != "/logout" and not AL_81549_Var.startswith("/static"):
        flash("Inicia sesión para continuar")
        return redirect("/login")
    # Si ya ha iniciado, no hacemos nada, es decir lo dejamos pasar



###############
# Inicio Codigo para agregar candidatos
##############

@app.route("/Candidato_Registro_1")
def Candidato_Registro_1():
    return render_template('Candidato_Registro.html')


@app.route("/Candidato_Registro_2", methods=['POST'])
def Candidato_Registro_2():
    if request.method == 'POST':
        #Se crean las variables y se guarda lo que viene del primer formulario
        AL_81549_Var = request.form['AL_81549_Var']
        AL_95175_Var = request.form['AL_95175_Var']
        AL_77296_Var = request.form['AL_77296_Var']
        AL_31325_Var = request.form['AL_31325_Var']
        AL_63624_Var = request.form['AL_63624_Var']
        AL_43532_Var = request.form['AL_43532_Var']
        AL_75432_Var = request.form['AL_75432_Var']
        AL_47518_Var = request.form['AL_47518_Var']
        AL_94939_Var = request.form['AL_94939_Var']

        #Conexion a la base de datos "Blockchain" y seleccion de la coleccion "Bloques"
        client = MongoClient('localhost', port=27017, username='', password='')
        db = client['VBlockchain']
        col = db['Bloques_opciones']

        #Se guarda en la variable "colvacia" si la coleccion "Bloques" esta vacia
        #colvacia = (col.count() == 0)
        colvacia = col.find_one({"AL_92466_Var": "1"})
        
        #Si "colvacia" es "None" el AL_59574_Var es "Genesis" y el AL_92466_Var es 1
        if(colvacia == None):
            AL_59574_Var = "Genesis"
            AL_92466_Var = 1
            AL_92466_Var = str(AL_92466_Var)
            #Se encripta toda la informacion con sha256 anexando el hash
            #encri = hashlib.sha256(AL_92466_Var.encode()+AL_81549_Var.encode()+AL_95175_Var.encode()
            #                       +AL_77296_Var.encode()+propuestas.encode()+descripcion.encode()+AL_59574_Var.encode())
            #AL_14229_Var = encri.hexdigest()
            AL_14229_Var = ph.hash(AL_92466_Var.encode()+AL_81549_Var.encode()+AL_95175_Var.encode()
                                   +AL_77296_Var.encode()+AL_31325_Var.encode()+AL_63624_Var.encode()
                                   +AL_43532_Var.encode()+AL_75432_Var.encode()+AL_47518_Var.encode()+AL_94939_Var.encode()+AL_59574_Var.encode())
            #Se insertan los valores en la base de datos
            col.insert_one({'AL_92466_Var': AL_92466_Var, 'AL_81549_Var': AL_81549_Var, 'AL_95175_Var': AL_95175_Var,
                        'AL_77296_Var': AL_77296_Var, 'AL_31325_Var': AL_31325_Var,'AL_63624_Var': AL_63624_Var,
                        'AL_43532_Var': AL_43532_Var,'AL_75432_Var': AL_75432_Var, 'AL_47518_Var': AL_47518_Var, 'AL_94939_Var': AL_94939_Var, 'AL_59574_Var': AL_59574_Var, 'AL_14229_Var': AL_14229_Var})
        
        #Si "colvacia" es DIFERENTE de "None" el AL_59574_Var es varia y el AL_92466_Var es depende de cuantos se hayan creado
        if (colvacia != None):
            #Se guarda en la variable "bloquecodificado" el ultimo bloque que se inserto
            bloquecodificado = col.find().sort('AL_92466_Var', -1).limit(1)
            #se recorren los items dentro de ese ultimo bloque 
            #cada item se guarda en la variable "bloqueanterior"
            for item in bloquecodificado :
                bloqueanterior = item
            #Dentro de la lista que se guardo en "bloqueanterior" se selecciona el campo "AL_92466_Var"
            numbloqant = bloqueanterior['AL_92466_Var']
            #Dentro de la lista que se guardo en "bloqueanterior" se selecciona el campo "AL_14229_Var"
            hashbloqant = bloqueanterior['AL_14229_Var']
            numbloqant= int(numbloqant)
            AL_92466_Var = numbloqant + 1
            AL_59574_Var = hashbloqant
            #Se convierten las variables en string para poderla guardar en la base de datos
            AL_92466_Var = str(AL_92466_Var)
            AL_59574_Var = str(AL_59574_Var)
            #Se encripta la informacion
            #encri = hashlib.sha256(AL_92466_Var.encode()+AL_81549_Var.encode()+AL_95175_Var.encode()
            #                       +AL_77296_Var.encode()+propuestas.encode()+descripcion.encode()+AL_59574_Var.encode())
            #AL_14229_Var = encri.hexdigest()
            AL_14229_Var = ph.hash(AL_92466_Var.encode()+AL_81549_Var.encode()+AL_95175_Var.encode()
                                   +AL_77296_Var.encode()+AL_31325_Var.encode()+AL_63624_Var.encode()
                                   +AL_43532_Var.encode()+AL_75432_Var.encode()+AL_47518_Var.encode()+AL_94939_Var.encode()+AL_59574_Var.encode())
            #Se insertan los valores en la base de datos
            col.insert_one({'AL_92466_Var': AL_92466_Var, 'AL_81549_Var': AL_81549_Var, 'AL_95175_Var': AL_95175_Var,
                        'AL_77296_Var': AL_77296_Var, 'AL_31325_Var': AL_31325_Var,'AL_63624_Var': AL_63624_Var,
                        'AL_43532_Var': AL_43532_Var,'AL_75432_Var': AL_75432_Var, 'AL_47518_Var': AL_47518_Var, 'AL_94939_Var': AL_94939_Var, 'AL_59574_Var': AL_59574_Var, 'AL_14229_Var': AL_14229_Var})
        
        #En formulario se retorna e imprime en pantalla la siguiente informacion
        return render_template('Candidato_Registro.html',AL_92466_Var= AL_92466_Var, AL_81549_Var=AL_81549_Var ,AL_95175_Var=AL_95175_Var , AL_77296_Var= AL_77296_Var ,
                               AL_31325_Var= AL_31325_Var , AL_63624_Var= AL_63624_Var,AL_43532_Var= AL_43532_Var,AL_75432_Var= AL_75432_Var,
                               AL_47518_Var= AL_47518_Var,AL_94939_Var= AL_94939_Var, AL_59574_Var=AL_59574_Var , AL_14229_Var=AL_14229_Var )


@app.route("/Candidato_Ver" , methods=['POST'])
#Luego de que activa el metodo 'POST' con la AL_81549_Var "/mostrar" corre la siguiente funcion
def Candidato_Ver():
    if request.method == 'POST':
        #Se conecta a la base de datos "Blockchain" y la coleccion "Bloques"
        client = MongoClient('localhost', port=27017, username='', password='')
        db = client['VBlockchain']
        col = db['Bloques_opciones']
        #Se consulta los bloques creados y se guarda en la variable "listabloques"
        lista_opciones = col.find()
        
    #Se publican las listas en el template Panilla_Mesa_Ver_Bloques.html
    return render_template('/Candidato_Ver.html', lista_opciones=lista_opciones)


###############
# Fin Codigo nuevo candidato
##############









###############
# Inicio de codigo de plantillas
##############
#Este codigo se ejecuta cuando se activa guardar los datos

@app.route("/Planilla_Mesa_Registro_1")
def Planilla_Mesa_Registro_1():
    return render_template('Planilla_Mesa_Registro.html')
    
@app.route("/Planilla_Mesa_Registro_2", methods=['POST'])
def Planilla_Mesa_Registro_2():
    if request.method == 'POST':
        #Se crean las variables y se guarda lo que viene del primer formulario
        AL_31165_Var= request.form['AL_31165_Var']
        AL_58961_Var = request.form['AL_58961_Var']
        AL_89655_Var = request.form['AL_89655_Var']
        AL_57895_Var = request.form['AL_57895_Var']
        AL_69175_Var = request.form['AL_69175_Var']
        AL_53671_Var = request.form['AL_53671_Var']
        AL_51198_Var = request.form['AL_51198_Var']
        AL_83665_Var = request.form['AL_83665_Var']
        AL_24633_Var = request.form['AL_24633_Var']
        AL_94939_Var_jurados = request.form['AL_94939_Var_jurados']
        
        #Conexion a la base de datos "Blockchain" y seleccion de la coleccion "Bloques"
        client = MongoClient('localhost', port=27017, username='', password='')
        db = client['VBlockchain']
        col = db['Bloques']

        #Se guarda en la variable "colvacia" si la coleccion "Bloques" esta vacia
        #colvacia = (col.count() == 0)
        colvacia = col.find_one({"AL_92466_Var": "1"})
        
        #Si "colvacia" es "None" el AL_59574_Var es "Genesis" y el AL_92466_Var es 1
        if(colvacia == None):
            AL_59574_Var = "Genesis"
            AL_92466_Var = 1
            AL_92466_Var = str(AL_92466_Var)
            #Se encripta toda la informacion con sha256 anexando el hash
            #encri = hashlib.sha256(AL_92466_Var.encode()+nombre_1.encode()+votacion_1.encode()
             #                      +nombre_2.encode()+votacion_2.encode()+AL_59574_Var.encode())
            AL_14229_Var = ph.hash(AL_92466_Var.encode()+AL_31165_Var.encode()+AL_58961_Var.encode()+AL_89655_Var.encode()+AL_57895_Var.encode()
                                   +AL_69175_Var.encode()+AL_53671_Var.encode()+AL_51198_Var.encode()+AL_83665_Var.encode()
                                   +AL_24633_Var.encode()+AL_94939_Var_jurados.encode()+AL_59574_Var.encode())
            #Se insertan los valores en la base de datos
            col.insert_one({'AL_92466_Var': AL_92466_Var, 'AL_31165_Var': AL_31165_Var,'AL_58961_Var': AL_58961_Var,
                            'AL_89655_Var': AL_89655_Var, 'AL_57895_Var': AL_57895_Var,
                            'AL_69175_Var': AL_69175_Var, 'AL_53671_Var': AL_53671_Var,'AL_51198_Var': AL_51198_Var,
                            'AL_83665_Var': AL_83665_Var,'AL_24633_Var': AL_24633_Var,
                            'AL_94939_Var_jurados': AL_94939_Var_jurados,'AL_59574_Var': AL_59574_Var, 'AL_14229_Var': AL_14229_Var })
        if (colvacia != None):
            bloquecodificado = col.find().sort('AL_92466_Var', -1).limit(1)
            #se recorren los items dentro de ese ultimo bloque 
            #cada item se guarda en la variable "bloqueanterior"
            for item in bloquecodificado :
                bloqueanterior = item
            #Dentro de la lista que se guardo en "bloqueanterior" se selecciona el campo "AL_92466_Var"
            numbloqant = bloqueanterior['AL_92466_Var']
            #Dentro de la lista que se guardo en "bloqueanterior" se selecciona el campo "AL_14229_Var"
            hashbloqant = bloqueanterior['AL_14229_Var']
            numbloqant= int(numbloqant)
            AL_92466_Var = numbloqant + 1
            AL_59574_Var = hashbloqant
            #Se convierten las variables en string para poderla guardar en la base de datos
            AL_92466_Var = str(AL_92466_Var)
            AL_59574_Var = str(AL_59574_Var)
            #Se encripta la informacion
            #encri = hashlib.sha256(AL_92466_Var.encode()+nombre_1.encode()+votacion_1.encode()+nombre_2.encode()
            #                   + votacion_2.encode()+AL_59574_Var.encode())
            #AL_14229_Var = encri.hexdigest()
            AL_14229_Var = ph.hash(AL_92466_Var.encode()+AL_31165_Var.encode()+AL_58961_Var.encode()+AL_89655_Var.encode()+AL_57895_Var.encode()
                                   +AL_69175_Var.encode()+AL_53671_Var.encode()+AL_51198_Var.encode()+AL_83665_Var.encode()
                                   +AL_24633_Var.encode()+AL_94939_Var_jurados.encode()+AL_59574_Var.encode())
            #Se insertan los valores en la base de datos
            col.insert_one({'AL_92466_Var': AL_92466_Var, 'AL_31165_Var': AL_31165_Var,'AL_58961_Var': AL_58961_Var,
                            'AL_89655_Var': AL_89655_Var, 'AL_57895_Var': AL_57895_Var,
                            'AL_69175_Var': AL_69175_Var, 'AL_53671_Var': AL_53671_Var,'AL_51198_Var': AL_51198_Var,
                            'AL_83665_Var': AL_83665_Var,'AL_24633_Var': AL_24633_Var,
                            'AL_94939_Var_jurados': AL_94939_Var_jurados,'AL_59574_Var': AL_59574_Var, 'AL_14229_Var': AL_14229_Var })
            
        return render_template('Planilla_Mesa_Registro.html', AL_92466_Var=AL_92466_Var ,AL_31165_Var=AL_31165_Var ,AL_58961_Var=AL_58961_Var ,
                               AL_89655_Var=AL_89655_Var , AL_57895_Var=AL_57895_Var ,
                               AL_69175_Var= AL_69175_Var , AL_53671_Var= AL_53671_Var , AL_51198_Var= AL_51198_Var, 
                               AL_83665_Var= AL_83665_Var , AL_24633_Var= AL_24633_Var , 
                               AL_94939_Var_jurados= AL_94939_Var_jurados , AL_59574_Var=AL_59574_Var , AL_14229_Var=AL_14229_Var)



@app.route("/Mostrar_Planillas" , methods=['POST'])
#Luego de que activa el metodo 'POST' con la AL_81549_Var "/mostrar" corre la siguiente funcion
def Mostrar_Planillas():
    if request.method == 'POST':
        #Se conecta a la base de datos "Blockchain" y la coleccion "Bloques"
        client = MongoClient('localhost', port=27017, username='', password='')
        db = client['VBlockchain']
        col = db['Bloques']
        #Se consulta los bloques creados y se guarda en la variable "listabloques"
        listabloques = col.find()
        
    #Se publican las listas en el template Panilla_Mesa_Ver_Bloques.html
    return render_template('/Planilla_Mesa_Ver_Bloques.html', listabloques=listabloques)


###############
# Fin Codigo nuevo de planilla por mesa
##############

###############
# Inicio Codigo nuevo de voto individual
##############

@app.route("/Voto_Individual_Registro_1")
def Voto_Individual_Registro_1():
    client = MongoClient('localhost', port=27017, username='', password='')
    db = client['VBlockchain']
    col = db['Bloques_opciones']
    lista_opciones_creadas = col.find()
    return render_template('Voto_Individual_Registro.html', lista_opciones_creadas = lista_opciones_creadas )



@app.route("/Voto_Individual_Registro_2", methods=['POST'])
def Voto_Individual_Registro_2():
    if request.method == 'POST':
        #Se crean las variables y se guarda lo que viene del primer formulario
        AL_18176_Var = request.form['AL_18176_Var']
        AL_97252_Var = request.form['AL_97252_Var']
        AL_67827_Var = request.form['AL_67827_Var']
        voto_AL_31165_Var = request.form['voto_AL_31165_Var']
        AL_34416_Var = request.form['AL_34416_Var']
        AL_72229_Var = request.remote_addr
        AL_59242_Var = request.headers.get('User-Agent')
        AL_34351_Var = datetime.now().isoformat()
        #Conexion a la base de datos "Blockchain" y seleccion de la coleccion "Bloques"
        client = MongoClient('localhost', port=27017, username='', password='')
        db = client['VBlockchain']
        col = db['Bloques_votos_individuales']

        #Se guarda en la variable "colvacia" si la coleccion "Bloques" esta vacia
        #colvacia = (col.count() == 0)
        colvacia = col.find_one({"AL_92466_Var": "1"})
        
        #Si "colvacia" es "None" el AL_59574_Var es "Genesis" y el AL_92466_Var es 1
        if(colvacia == None):
            AL_59574_Var = "Genesis"
            AL_92466_Var = 1
            AL_92466_Var = str(AL_92466_Var)
            #Se encripta toda la informacion con sha256 anexando el hash
            #encri = hashlib.sha256(AL_92466_Var.encode()+AL_18176_Var.encode()+AL_97252_Var.encode()
            #                       +AL_67827_Var.encode()+voto_AL_31165_Var.encode()+AL_34416_Var.encode()+AL_59574_Var.encode())
            #AL_14229_Var = encri.hexdigest()
            AL_14229_Var = ph.hash(AL_92466_Var.encode()+AL_18176_Var.encode()+AL_97252_Var.encode()
                                   +AL_67827_Var.encode()+voto_AL_31165_Var.encode()+AL_34416_Var.encode()+AL_72229_Var.encode()
                                   +AL_59242_Var.encode()+AL_34351_Var.encode()+AL_59574_Var.encode())
            #Se insertan los valores en la base de datos
            col.insert_one({'AL_92466_Var': AL_92466_Var, 'AL_18176_Var': AL_18176_Var, 'AL_97252_Var': AL_97252_Var,
                        'AL_67827_Var': AL_67827_Var, 'voto_AL_31165_Var': voto_AL_31165_Var, 'AL_34416_Var': AL_34416_Var,
                        'AL_72229_Var': AL_72229_Var,'AL_59242_Var': AL_59242_Var,'AL_34351_Var': AL_34351_Var, 
                        'AL_59574_Var': AL_59574_Var, 'AL_14229_Var': AL_14229_Var })
        
        #Si "colvacia" es DIFERENTE de "None" el AL_59574_Var es varia y el AL_92466_Var es depende de cuantos se hayan creado
        if (colvacia != None):
            #Se guarda en la variable "bloquecodificado" el ultimo bloque que se inserto
            bloquecodificado = col.find().sort('AL_92466_Var', -1).limit(1)
            #se recorren los items dentro de ese ultimo bloque 
            #cada item se guarda en la variable "bloqueanterior"
            for item in bloquecodificado :
                bloqueanterior = item
            #Dentro de la lista que se guardo en "bloqueanterior" se selecciona el campo "AL_92466_Var"
            numbloqant = bloqueanterior['AL_92466_Var']
            #Dentro de la lista que se guardo en "bloqueanterior" se selecciona el campo "AL_14229_Var"
            hashbloqant = bloqueanterior['AL_14229_Var']
            numbloqant= int(numbloqant)
            AL_92466_Var = numbloqant + 1
            AL_59574_Var = hashbloqant
            #Se convierten las variables en string para poderla guardar en la base de datos
            AL_92466_Var = str(AL_92466_Var)
            AL_59574_Var = str(AL_59574_Var)
            #Se encripta la informacion
            #encri = hashlib.sha256(AL_92466_Var.encode()+AL_18176_Var.encode()+AL_97252_Var.encode()
            #                       +AL_67827_Var.encode()+voto_AL_31165_Var.encode()+AL_34416_Var.encode()+AL_59574_Var.encode())
            #AL_14229_Var = encri.hexdigest()
            AL_14229_Var = ph.hash(AL_92466_Var.encode()+AL_18176_Var.encode()+AL_97252_Var.encode()
                                   +AL_67827_Var.encode()+voto_AL_31165_Var.encode()+AL_34416_Var.encode()+AL_72229_Var.encode()
                                   +AL_59242_Var.encode()+AL_34351_Var.encode()+AL_59574_Var.encode())
            #Se insertan los valores en la base de datos
            col.insert_one({'AL_92466_Var': AL_92466_Var, 'AL_18176_Var': AL_18176_Var, 'AL_97252_Var': AL_97252_Var,
                        'AL_67827_Var': AL_67827_Var, 'voto_AL_31165_Var': voto_AL_31165_Var, 'AL_34416_Var': AL_34416_Var,
                        'AL_72229_Var': AL_72229_Var,'AL_59242_Var': AL_59242_Var,'AL_34351_Var': AL_34351_Var, 
                        'AL_59574_Var': AL_59574_Var, 'AL_14229_Var': AL_14229_Var })
        #En formulario se retorna e imprime en pantalla la siguiente informacion
        return render_template('Voto_Individual_Registro.html',AL_92466_Var= AL_92466_Var, AL_18176_Var=AL_18176_Var,
                               AL_97252_Var=AL_97252_Var, AL_67827_Var= AL_67827_Var, voto_AL_31165_Var= voto_AL_31165_Var , 
                               AL_34416_Var= AL_34416_Var, AL_72229_Var= AL_72229_Var,AL_59242_Var= AL_59242_Var,
                               AL_34351_Var= AL_34351_Var,AL_59574_Var=AL_59574_Var, AL_14229_Var=AL_14229_Var )


@app.route("/Voto_Individual_Ver" , methods=['POST'])
#Luego de que activa el metodo 'POST' con la AL_81549_Var "/mostrar" corre la siguiente funcion
def subirinfovoto():
    if request.method == 'POST':
        #Se conecta a la base de datos "Blockchain" y la coleccion "Bloques"
        client = MongoClient('localhost', port=27017, username='', password='')
        db = client['VBlockchain']
        col = db['Bloques_votos_individuales']
        #Se consulta los bloques creados y se guarda en la variable "listabloques"
        listabloques_indv = col.find()
        
    #Se publican las listas en el template Panilla_Mesa_Ver_Bloques.html
    return render_template('/Voto_Individual_Ver.html', listabloques_indv=listabloques_indv)


###############
# Fin Codigo nuevo  de voto individual
##############





###############
# Inicio Codigo de la grafica
##############

# AL_81549_Var principal de Flask
@app.route("/Grafica_Dinamica")
def Graficas_Dinamica():
    client = MongoClient('localhost', port=27017, username='', password='')
    db = client['VBlockchain']
    col = db['Bloques']
    #Se consulta los bloques creados y se guarda en la variable "listabloques"
    colvacia2 = col.find_one({"AL_92466_Var": "1"})
    # Dataset de ejemplo
    df = pd.DataFrame([colvacia2]) 
    # Convertir votaciones a números
    df['AL_57895_Var'] = pd.to_numeric(df['AL_57895_Var'])
    df['AL_69175_Var'] = pd.to_numeric(df['AL_69175_Var'])
    # Reorganizar datos para gráfico
    df_votos = pd.DataFrame({
        'Nombre': [df['AL_89655_Var'][0], df['AL_69175_Var'][0]],
        'Votos': [df['AL_57895_Var'][0], df['AL_53671_Var'][0]]
        })
    # Crear gráfico
    fig = px.bar(df_votos, x='Nombre', y='Votos', title='Resultados de Votación')
    dash_app.layout = html.Div([
        html.H1("Dashboard Interactivo", style={"textAlign": "center"}),
        dcc.Graph(figure=fig)
        ])
    return render_template_string("""
    <h1>Grafica de la votacion total</h1>
    <p>Grafica de barras sobre el  <a href="/dashboard/">Total votos</a></p>
    """)

###############
# Fin Codigo de la grafica
##############


###############
# CODIGO DE CONFIRMAR DATOS
##############

@app.route("/Confirmar_Votos_1" , methods=['POST'])
#Luego de que activa el metodo 'POST' con la AL_81549_Var "/mostrar" corre la siguiente funcion
def Confirmar_Votos_1():
    #Se publican las listas en el template Panilla_Mesa_Ver_Bloques.html
    return render_template('/Confirmar_Votos_1.html')

@app.route("/Confirmar_Votos_2" , methods=['POST'])
def Confirmar_Votos_2():
    if request.method == 'POST':
        #Se conecta a la base de datos "Blockchain" y la coleccion "Bloques"
        client = MongoClient('localhost', port=27017, username='', password='')
        db = client['VBlockchain']
        #Se crean las variables y se guarda lo que viene del primer formulario
        AL_76582_Var = request.form['AL_76582_Var']
        AL_67827_Var = request.form['AL_67827_Var']

        AL_76582_Var = str(AL_76582_Var)
        AL_67827_Var = str(AL_67827_Var)

        # Colecciones
        totales = db["Bloques"]
        total_voto_individuales = db["Bloques_votos_individuales"]

        # Obtener el total esperado desde la colección 'totales'
        documento_total = totales.find_one({"AL_92466_Var":AL_76582_Var})
        votacion_1_string = documento_total["AL_57895_Var"] if documento_total else 0
        votacion_2_string = documento_total["AL_53671_Var"] if documento_total else 0

        votacion_1 = int(votacion_1_string)
        votacion_2 = int(votacion_2_string)
        votacion_total = votacion_1 + votacion_2

        # Contar documentos en 'items' con ese tipo
        conteo_items = total_voto_individuales.count_documents({"AL_67827_Var": AL_67827_Var})
        total_voto_individual = int(conteo_items)

        if votacion_total == total_voto_individual:
            concuerda = "Si"
        if votacion_total != total_voto_individual:
            concuerda = "No"

        
    #Se publican las listas en el template Panilla_Mesa_Ver_Bloques.html
    return render_template('/Confirmar_Votos_2.html', votacion_total=votacion_total, total_voto_individual=total_voto_individual, concuerda=concuerda)

###############
# FIN CODIGO DE CONFIRMAR DATOS
##############






# Iniciar el servidor
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8000, debug=True)




