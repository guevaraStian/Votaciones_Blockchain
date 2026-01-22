

<h1 style="font-size: 3em; color: #FF0000;">•  VOTACIONES CON BLOCKCHAIN EN PYTHON Y MONGO DB </h1> 

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![JavaScrip](https://shields.io/badge/JavaScript-F7DF1E?logo=JavaScript&logoColor=000&style=flat-square)
![Flask](https://img.shields.io/badge/Flask-000000?style=for-the-badge&logo=Flask&logoColor=white) 
![Bootstrap](https://img.shields.io/badge/Bootstrap-563D7C?style=for-the-badge&logo=bootstrap&logoColor=white)
![MongoDB](https://img.shields.io/badge/-MongoDB-13aa52?style=for-the-badge&logo=mongodb&logoColor=white)

Los pasos para poner en ejecución son los siguientes
Ir a la pagina web de Python y Git, luego descargarlo para tu sistema operativo, escoger la opción "add path" con el fin de poder ejecutar comandos de Python en la terminal de comandos : 

```Pagina web
https://www.python.org/downloads/
https://git-scm.com/downloads
```
Vamos a la pagina web de MongoDb y descargamos el ejecutable y lo ejecutamos, luego de finalizar la instalación abrimos el Compass de MongoDb.

```Pagina web
https://www.mongodb.com/es/products/tools/compass
```
Luego de tener instalado Python podemos ejecutar los siguientes comandos en la carpeta del proyecto.

```Terminal de comandos
python --version
pip --version
git init
git clone https://github.com/guevaraStian/Votaciones_Blockchain.git
cd Votaciones_Blockchain
git push origin master
```

Luego ingresamos a la carpeta creada e instalamos las librerias y ejecutamos el proyecto.

```Terminal de comandos
pip install flask hashlib flask_bootstrap dash plotly pandas argon2 
python main.py
```
Luego que el proyecto ya se este ejecutando, podemos verlo funcionar en la siguiente ruta url.

```Pagina web
http://localhost:8000
http://127.0.0.1:8000
```


<h2 style="font-size: 3em; color: #FF0000;">•  El software funcionando </h2> 


El software tiene ingresos de informacion para los siguientes datos: candidatos, planillas de votacion por mesa y voto individual.


A continuacion ejemplo de ingreso de datos de candidato: 
![Imagen1](images/Imagen1.png)


En la siguiente imagen se muestra las planillas de votacion por mesa creadas en el software:
![Imagen2](images/Imagen2.png)


En esta tercer imagen se muestra como se registra el voto individual, en este caso voto de pais, de departamento y de municipio.
![Imagen3](images/Imagen3.png)


En el voto individual se guarda la ip del votante, tambien el sistema operativo desde donde vota, hora de votacion y todo esto en tambien va dentro del hash criptografico actual, como se muestra en la siguiente imagen.
![Imagen4](images/Imagen4.png)