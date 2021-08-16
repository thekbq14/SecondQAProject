from flask import Flask, request, jsonify

app = Flask(__name__)

times = {
    'city' : {
        'Cardiff' : 3.0,
        'Glasgow' : 7.0,
        'Manchester' : 4.15
    }

    'transport' : {
        'Train' : 0.5,
        'Plane' : 0.25,
        'Coach' : 1
    }
}

@app.route('/post/time', methods=['POST'])
def post_time():
    city = request.json['city']
    transport = request.json['transport']

    time = times['city'][city] * times['transport'][transport] + "hours"
    time = round(time, 2)

    return jsonify(price)

if __name__ == '__main__':
    app.run(host='0.0.0.0')