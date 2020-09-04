# SemVisorIA 👁️ 🚦
Interfaz para pruebas del modelo generado para la detección del estado de un semaforo.

Para levantar en un ambiente local en Windows, necesitará tener instalado lo siguiente:
* Python 3
*	Editor de código de su preferencia.

A continuación Abrir una terminal “command prompt” y ejecutar el siguiente comando:
```
python -m venv myvenv
```
Una vez creado el entorno virtual, lo iniciamos con el siguiente comando:
```
myvenv\Scripts\activate
```
Sabremos que estamos dentro del entorno virtual cuando veamos que la línea de comando en consola tiene el prefijo (myvenv).
Ahora necesitamos instalar todas las dependencias que necesita nuestro proyecto. 
Para realizar esto, debemos asegurarnos de tener la última versión de pip.
en consola ejecutamos:
```
python -m pip install --upgrade pip 
```
Luego ingresamos a la carpeta donde está nuestro codigo:
```
cd SemVisorIA
```
Y ejecutamos:
```
pip install -r requirements.txt
```
Luego debemos ejecutar las migraciones de nuestro proyecto, Dentro del entorno virtual, ejecutamos los siguientes comandos:
```
python manage.py makemigrations
python manage.py migrate
```
Cuando se haga ejecutado todas las migraciones, se procede a levantar el servidor:
```
python manage.py runserver
```
#### En nuestro navegador, ingresamos a la url http://127.0.0.1:8000 y veremos nuestro proyecto ejecutándose.

