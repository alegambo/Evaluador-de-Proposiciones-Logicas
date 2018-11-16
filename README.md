# Evaluador-de-Proposiciones-Logicas
Aplicacion Rest-Api que realiza una evaluación en Logica Proposicional. Servidor en Python(Django) y cliente en Vue.js.

Realizada en Colaboración con el Profesor Carlos Loria Saenz de la Universidad Nacional de Costa Rica.

Se asume como átomos lógicos unicamente True, False
# Tools para servidor y api:
Python 3.6

Activar Ambiente virtual de windows ubicado en Servidor/ProyectoParadigmas/proyecto, si es Linux realizar ambiente nuevo.

Instalar Django(pip install django).

Instalar RestFramework(pip install djangorestframework).

Instalar Django Cors(pip install django-cors-headers).

Instalar Antlr(pip install anlr4-python3-runtime).

Correr el servidor ubicado en Servidor/ProyectoParadigmas/proyecto1 mediante el comando python manage.py runserver
# Tools para Cliente
Instalar Node y npm

Instalar Vue.js cli.

Ejecutar el cliente ubicandose en la carpeta propuesta-cliente, mediante el comando npm run serve, se levanta el servidor.

Verificar cual puerto levantó el servidor del cliente y modificar el archivo C:\Users\Hewlett Packard\Desktop\Evaluador-de-Proposiciones-Logicas\Servidor\ProyectoParadigmas\proyecto1\proyecto1\settings.py en la linea 127, cambiando el CORS_ORIGIN_WHITELIST = 'localhost:8081' por el puerto que se levantó en su máquina.




