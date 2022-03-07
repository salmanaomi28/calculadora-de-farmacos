from distutils.log import debug
from flask import Flask
from flask import Flask, jsonify

app = Flask(__name__)


@app.route("/dosis/<string:peso>/<string:dosisTerapeutica>")
def get_datosD(peso,dosisTerapeutica):
    peso = float(peso)
    dosisTerapeutica = float(dosisTerapeutica)
    dosis = dosisTerapeutica * peso
    return jsonify({ "dosis" : dosis})


@app.route("/suspension/<string:presentacion>/<string:dosisTerapeutica>/<string:diluyente>")
def get_datosM(presentacion,diluyente, dosisTerapeutica):
    dosisTerapeutica = float(dosisTerapeutica)
    diluyente = float(diluyente)
    presentacion = float(presentacion)
    suspension = dosisTerapeutica * diluyente / presentacion
    return jsonify({"suspension": suspension})

@app.route("/dosisPordia/<string:dosisTerapeutica>/<string:peso>/<string:horasM>")
def get_datosM(cc, peso,dosisTerapeutica, horasM):
    dosis = float(dosis)
    cc = float(cc)
    dosisTerapeutica = float(dosisTerapeutica)
    peso = float(peso)
    horasM = float(horasM)
    dosis = dosisTerapeutica * peso
    cc = 24 / horasM
    dosisPordia = dosis / cc
    return jsonify({"dosisPorDia": dosisPordia})

if __name__ == '_main_':
    app.run(debug=True, port=6000)