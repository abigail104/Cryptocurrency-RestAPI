from flask import Flask, jsonify, abort, make_response, request

app = Flask(__name__)

cryptocurrencies = [
        {
            'id' : 1,
            'name' : u'Bitcoin',
            'price' : u'$11,266.87'
        },
        {

            'id' : 2,
            'name' : u'Ethereum',
            'price' :u'$426.11'
        },
        {
        
            'id' : 3,
            'name' : u'Tether',
            'price' :u'$1.00'
        }
        
]

@app.route('/', methods=['GET'])
def get_cryptocurrency():
    return jsonify({'cryptocurrency': cryptocurrencies})

@app.route('/cryptocurrency/<int:cryptocurrency_id>', methods=['GET'])
def get_crypto(cryptocurrency_id):
    cryptocurrency = [cryptocurrency for cryptocurrency in cryptocurrencies if cryptocurrency['id'] == cryptocurrency_id]
    if len(cryptocurrency) == 0:
        abort(404)
    return jsonify({'cryptocurrency' : cryptocurrency[0]})

#@app.errorhandler(404)
#def not_found(error):
#    return make_response(jsonify({'error': 'Not found'}), 404)

@app.route('/', methods=['POST'])
def create_crypto():
    if not request.json or not 'name' in request.json:
        abort(400)
    cryptocurrency = {
            'id': cryptocurrencies[-1]['id'] + 1,
            'name': request.json['name'],
            'price': request.json.get('price',"")

            }
    cryptocurrencies.append(cryptocurrency)
    return jsonify({'cryptocurrency': cryptocurrency}),201

@app.route('/<int:cryptocurrency_id>', methods=['PUT'])
def update_crypto(cryptocurrency_id):
    cryptocurrency = [cryptocurrency for cryptocurrency in cryptocurrencies if cryptocurrency['id'] == cryptocurrency_id]
    if len(cryptocurrency) == 0:
        abort(404)
    if not request.json:
        abort(400)
    if 'name' in request.json and type(request.json['name']) != str:
        abort(400)
    if 'price' in request.json and type(request.json['price']) is not str:
        abort(400)
    cryptocurrency[0]['name'] = request.json.get('name',cryptocurrency[0]['name'])
    cryptocurrency[0]['price'] = request.json.get('price', cryptocurrency[0]['price'])
    return jsonify({'cryptocurrency': cryptocurrency[0]})

@app.route('/cryptocurrency/<int:cryptocurrency_id>', methods=['DELETE'])
def delete_crypto(cryptocurrency_id):
    cryptocurrency = [cryptocurrency for cryptocurrency in cryptocurrencies if cryptocurrency['id'] == cryptocurrency_id]
    if len(cryptocurrency) == 0:
        abort(404)
    cryptocurrencies.remove(cryptocurrency[0])
    return jsonify({'cryptocurrency': cryptocurrency[0]})

if __name__ == '__main__':
    app.run(debug=True)
       
