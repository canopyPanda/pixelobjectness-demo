from flask import Flask, request, Response
from flask_cors import CORS
import json


def serve(func, func1, func2, func3, func4, func5, host='0.0.0.0', port=3000):
    app = Flask(__name__)
    CORS(app, max_age=3600)

    @app.route('/predict', methods=['POST'])
    def predict():
        input = request.files['image'].read()
        return_mask = 'mask' in request.values
        image = func(input, return_mask)
        return Response(
            image,
            mimetype='image/jpeg')
    
    @app.route('/conv1', methods=['POST'])
    def conv1():
        input = request.files['image'].read()
        image = func1(input)
        return Response(
            image,
            mimetype='image/jpeg')
    
    @app.route('/conv2', methods=['POST'])
    def conv2():
        input = request.files['image'].read()
        image = func2(input)
        return Response(
            image,
            mimetype='image/jpeg')
    
    @app.route('/conv3', methods=['POST'])
    def conv3():
        input = request.files['image'].read()
        image = func3(input)
        return Response(
            image,
            mimetype='image/jpeg')
    
    @app.route('/conv4', methods=['POST'])
    def conv4():
        input = request.files['image'].read()
        image = func4(input)
        return Response(
            image,
            mimetype='image/jpeg')
    
    @app.route('/conv5', methods=['POST'])
    def conv5():
        input = request.files['image'].read()
        image = func5(input)
        return Response(
            image,
            mimetype='image/jpeg')
    app.run(host=host, port=port, threaded=False)

from flask import Flask, request, Response
from flask_cors import CORS
import json


def serve(func, func1, func2, func3, func4, func5, host='0.0.0.0', port=3000):
    app = Flask(__name__)
    CORS(app, max_age=3600)

    @app.route('/predict', methods=['POST'])
    def predict():
        input = request.files['image'].read()
        return_mask = 'mask' in request.values
        image = func(input, return_mask)
        return Response(
            image,
            mimetype='image/jpeg')
    
    @app.route('/conv1', methods=['POST'])
    def conv1():
        input = request.files['image'].read()
        image = func1(input)
        return Response(
            image,
            mimetype='image/jpeg')
    
    @app.route('/conv2', methods=['POST'])
    def conv2():
        input = request.files['image'].read()
        image = func2(input)
        return Response(
            image,
            mimetype='image/jpeg')
    
    @app.route('/conv3', methods=['POST'])
    def conv3():
        input = request.files['image'].read()
        image = func3(input)
        return Response(
            image,
            mimetype='image/jpeg')
    
    @app.route('/conv4', methods=['POST'])
    def conv4():
        input = request.files['image'].read()
        image = func4(input)
        return Response(
            image,
            mimetype='image/jpeg')
    
    @app.route('/conv5', methods=['POST'])
    def conv5():
        input = request.files['image'].read()
        image = func5(input)
        return Response(
            image,
            mimetype='image/jpeg')
    app.run(host=host, port=port, threaded=False)


