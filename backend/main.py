# Importing flask module in the project is mandatory
# An object of Flask class is our WSGI application.
from flask import Flask, jsonify, request, Response
from fis import *
from flask_cors import CORS, cross_origin

# Flask constructor takes the name of
# current module (__name__) as argument.
app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

# The route() function of the Flask class is a decorator,
# which tells the application which URL should call
# the associated function.
@app.route('/')
@cross_origin()

# ‘/’ URL is bound with hello_world() function.
def hello_world():
    return jsonify({'message': 'Tingkat kepuasan pelanggan'})

@app.route('/predict', methods=['POST'])
@cross_origin()

def get_crips():
    data = request.get_json()
    # print(data)
    # if not isinstance(data['kualitas_makanan'], float) or not isinstance(data['kecepatan_layanan'], float):
    #     return Response("{'error':'must be float'}", status=401, mimetype='application/json')
    fuzz_kualitas_makanan_api, fuzz_kecepatan_layanan_api = fuzzification(input_val={"kualitas_makanan": data['kualitas_makanan'], "kecepatan_layanan": data['kecepatan_layanan']})
    infer_tidak_puas_api, infer_puas_api = inference(fuzz_kualitas_makanan_api, fuzz_kecepatan_layanan_api)
    result_api = defuzzification(infer_tidak_puas_api, infer_puas_api)

    derajat_kualitas = {}
    derajat_kecepatan = {}
    kualitas_makanan_ling = ["buruk", "sedang", "baik"]
    kecepatan_layanan_ling = ["cepat", "lambat"]
    for i, item in enumerate(fuzz_kualitas_makanan_api):
        derajat_kualitas[kualitas_makanan_ling[i]] = item

    for i, item in enumerate(fuzz_kecepatan_layanan_api):
        derajat_kecepatan[kecepatan_layanan_ling[i]] = item

    return jsonify({ "hasil": result_api, "derajat_kualitas": derajat_kualitas, "derajat_kecepatan": derajat_kecepatan })

# main driver function
if __name__ == '__main__':

    # run() method of Flask class runs the application
    # on the local development server.
    app.run()
