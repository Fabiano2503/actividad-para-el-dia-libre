from flask import Flask, render_template, request
import requests

app = Flask(__name__)

app.config['SECRET_KEY'] = '12345678'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/actividad', methods=['GET'])
def actividad():
    # OBTENER PARAMETRO 'TYPE' DE LA URL
    actividad_type = request.args.get('type')

    # URL DE LA API
    url_api = 'http://bored.api.lewagon.com/api/activity/'

    if actividad_type:
        # SI HAY TIPO DE ACTIVIDAD AGREGARLO A LA URL
        url = f'{url_api}?type={actividad_type}'
    else:
        # SI NO HAY GENERAR ACTIVIDAD ALEATORIA
        url = url_api

    # SOLICITUD A LA API
    response = requests.get(url)

    if response.status_code == 200:
        # OBTENER LOS DATOS EN JSON
        actividad_data = response.json()
        # FILTRAR SOLO LA ACTIVIDAD Y SI NO SE ENCUENTRA SE MANDA UN MENSAJE
        actividad = actividad_data.get('activity', 'No se encontro actividad')
    else:
        # MANDAR MENSAJE SI HUBO ERROR EN LA SOLICITUD
        actividad = 'Error al recibir la actividad'

    # MOSTRAR ACTIVIDAD
    return actividad

if __name__ == '__main__':
    app.run(debug=True)