from flask import Flask
from distutils.log import debug
from flask import Flask, jsonify

app = Flask(__name__)


@app.route("/dosis/<string:peso>/<string:dosisTerapeutica>")
def get_datosD(peso,dosisTerapeutica):
    peso = float(peso)
    dosisTerapeutica = float(dosisTerapeutica)
    dosis = dosisTerapeutica * peso
    return jsonify({ "dosis" : dosis})


@app.route("/suspension/<string:peso>/<string:presentacion>/<string:dosisTerapeutica>/<string:diluyente>")
    dosisTerapeutica = float(dosisTerapeutica)
    diluyente = float(diluyente)
    peso = float(peso)
    presentacion = float(presentacion)
    dosis = dosisTerapeutica * peso
    suspension = dosisTerapeutica * diluyente / presentacion
    return jsonify({"suspension": suspension})

@app.route("/dosisPordia/<string:dosisTerapeutica>/<string:peso>/<string:horasM>")
def get_datosM2( peso,dosisTerapeutica, horasM):
   
    dosisTerapeutica = float(dosisTerapeutica)
    peso = float(peso)
    horasM = float(horasM)
    dosis = dosisTerapeutica * peso
    cc = 24 / horasM
    dosisPorDia = dosis / cc
    return jsonify({ 
                     "dosis": dosis,
                    "cc": cc,
                    "dosisPorDia":dosisPorDia
                   }
                   
                  )

if __name__ == '_main_':
    app.run(debug=True, port=4000)
