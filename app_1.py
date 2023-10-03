from flask import Flask, request, jsonify, render_template
from flask_cors import CORS, cross_origin
from NB_Model.model_NB import nb_response

app = Flask(__name__)
CORS(app)  # Enable CORS for the entire application

@app.route('/')
@cross_origin()  # Enable CORS for this specific route
def index():
    # do something...
    return render_template('view.html')

@app.route('/to_model_NB', methods=['POST'])
@cross_origin()  # Enable CORS for this specific route
def respond_to_try():
    message = request.json['message']
    response, tag = nb_response(message)
    return jsonify({'res': response, 'tag': tag})

@app.route('/test', methods=['POST'])
@cross_origin()  # Enable CORS for this specific route
def test():
    message = request.json['message']
    response = '[Port: /test] success'
    print('Prot: /test, Get: ', message)
    tag = 'test'
    return jsonify({'res': response, 'tag': tag})


if __name__ == '__main__':
    app.run(debug=True)
