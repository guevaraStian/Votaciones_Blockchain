Votaciones con Blockchain


![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![JavaScrip](https://shields.io/badge/JavaScript-F7DF1E?logo=JavaScript&logoColor=000&style=flat-square)
![Flask](https://img.shields.io/badge/Flask-000000?style=for-the-badge&logo=Flask&logoColor=white) 
![Bootstrap](https://img.shields.io/badge/Bootstrap-563D7C?style=for-the-badge&logo=bootstrap&logoColor=white)
![MongoDB](https://img.shields.io/badge/-MongoDB-13aa52?style=for-the-badge&logo=mongodb&logoColor=white)

Los pasos para poner en ejecución son los siguientes
Ir a la pagina web de Python y descargarlo para tu sistema operativo, escoger la opción "add path" con el fin de poder ejecutar comandos de Python en la terminal de comandos

```Pagina web
https://www.python.org/downloads/
```
Vamos a la pagina web de MongoDb y descargamos el ejecutable y lo ejecutamos, luego de finalizar la instalación abrimos el Compass de MongoDb

```Pagina web
https://www.mongodb.com/es/products/tools/compass
```
Luego de tener instalado Python podemos ejecutar los siguientes comandos en la carpeta del proyecto

```Terminal de comandos
python --version
pip --version
git init
git clone https://github.com/guevaraStian/Votaciones_Blockchain.git
git push origin master
```

Luego ingresamos a la carpeta creada e instalamos las librerias y ejecutamos el proyecto.

```Terminal de comandos
pip install flask werkzeug lxml hashlib pymongo
python main.py
```
Luego que el proyecto ya se este ejecutando, podemos verlo funcionar en la siguiente ruta url

```Pagina web
http://localhost:8000
http://127.0.0.1:8000
```
