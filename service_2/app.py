from flask import Flask
import random

app = Flask(__name__)

city = ['Cardiff', 'Glasgow', 'Manchester']

@app.route('/get/city')
def get_city():
    return random.choice(city)


if __name__ == '__main__':
    app.run(host='0.0.0.0')