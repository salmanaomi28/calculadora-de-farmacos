from flask import Flask
from distutils.log import debug
from flask import Flask, jsonify

app = Flask(__name__)


@app.route("/dosis/<string:peso>/<string:dosisT>")
def get_datosD(peso,dosisT):
    peso = float(peso)
    dosisT = float(dosisT)
    dosis = dosisT * peso
    return jsonify({ "dosis" : dosis})


@app.route("/susp/<string:peso>/<string:mg>/<string:dosisT>/<string:ml>")
    def get_datosM(peso,mg,dosisT, ml):
    dosisT = float(dosisT)
    ml = float(ml)
    peso = float(peso)
    dosis = float(dosis)
    mg = float(mg)
    dosis = dosisT * peso
    susp = dosisT * ml / mg
    return jsonify({"susp": susp})

@app.route("/dosisPordia/<string:dosisT>/<string:peso>/<string:horasM>")
def get_datosM2(peso,dosisT, horasM):
    cc = float(0)
    dosisT = float(dosisT)
    peso = float(peso)
    horasM = float(horasM)
    dosis = dosisT * peso
    cc = 24 / horasM
    dosisPorDia = dosis / cc
    return jsonify({"dosisPorDia":dosisPorDia})

if __name__ == '__main__':
    app.run(debug=True, port=4000)
