from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "Nueva versión desplegada automáticamente con Jenkins CI/CD, De nuevo cambios echos por Cesar Avalos desde VSC"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
