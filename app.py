from distutils.log import debug
from flask import Flask
from flask import Flask, jsonify

app = Flask(_name_)


@app.route("/dosis/<string:peso>/<string:dosisT>")
def get_datosD(peso,dosisT):
    peso = float(peso)
    dosisT = float(dosisT)
    dosis = dosisT * peso
    return jsonify({"dosis" : dosis})


@app.route("/suspension/<string:peso/<string:mg>/<string:dosisT>/<string:ml>")
def get_DatosM(peso, mg, dosisT, ml):
    peso = float(peso)
    mg = float(mg)
    dosisT = float(dosisT)
    ml = float(ml)
    dosis = float(0)
    dosis = dosisT * peso
    suspension = dosis * (ml/mg)
    return jsonify({"suspension" : suspension})



@app.route("/dosisDia/<string:dosisT>/<string:peso>/<string:peso>/<string:horasM>")
def get_dosisDia(dosisT,peso,horasM):
    dosisT = float(dosisT)
    peso = float(peso)
    horasM = float(horasM)
    cc = float(0)
    cc = 24 / horasM
    dosisDia = dosis / cc
    return jsonify({"dosisDia" : dosisDia})



if _name_ == '__main__':
    app.run(debug=True, port=4000)
