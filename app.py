from flask import Flask

app = Flask(__name__)

app.config['SECRET_KEY'] = '12345678'

@app.route('/')
def index():
    return "Ruta Principal"

if __name__ == '__main__':
    app.run(debug=True)