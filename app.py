from flask import Flask, render_template, request
import requests

app = Flask(__name__)

app.config['SECRET_KEY'] = '12345678'

historial_actividades = []

@app.route('/')
def index():
    return render_template('index.html', historial=historial_actividades)

@app.route('/actividad', methods=['GET'])
def actividad():
    # OBTENER PARAMETRO 'TYPE' DE LA URL
    actividad_type = request.args.get('type')

    # URL DE LA API
    url_api = 'http://bored.api.lewagon.com/api/activity/'

    # CONCATENAR URL SEGUN SI SE ESPECIFICA UN TIPO DE ACTIVIDAD O NO
    url = f'{url_api}?type={actividad_type}' if actividad_type else url_api
    
    try:
        # SOLICITUD A LA API
        response = requests.get(url)
        # VERIFICAR SI LA RESPUESTA FUE EXITOSA (STATUS CODE 200)
        response.raise_for_status()
    
        # CONVERTIR LOS DATOS JSON EN UN DICCIONARIO
        actividad_data = response.json()
        # FILTRAR SOLO LA ACTIVIDAD Y SI NO SE ENCUENTRA SE MANDA UN MENSAJE
        actividad = actividad_data.get('activity', 'No se encontro actividad')

        # AGREGAR LA ACTIVIDAD AL HISTORIAL
        historial_actividades.append({"actividad": actividad, "tipo": actividad_type})

    except requests.exceptions.RequestException as e:
        # MANEJAR ERRORES RELACIONADOS CON LA SOLICITUD
        actividad = f'Error al realizar la solicitud a la API: {str(e)}'

    # MOSTRAR ACTIVIDAD
    return render_template('index.html', actividad=actividad, historial=historial_actividades)

if __name__ == '__main__':
    app.run(debug=True)