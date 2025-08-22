from flask import Flask, render_template

app = Flask(__name__)

app.config['SECRET_KEY'] = '12345678'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/actividad', methods=['GET'])
def actividad():
    # URL DE LA API: 'http://bored.api.lewagon.com/api/activity/'
    return "Ruta Actividad"

if __name__ == '__main__':
    app.run(debug=True)