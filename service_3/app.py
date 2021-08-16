from flask import Flask
import random

app = Flask(__name__)

transport = ['Train', 'Plane', 'Coach']

@app.route('/get/transport')
def get_transport():
    return random.choice(transport)


if __name__ == '__main__':
    app.run(host='0.0.0.0')