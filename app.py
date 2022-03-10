from distutils.log import debug
from flask import Flask
from flask import Flask, jsonify
import math

app = Flask(__name__)

@app.route("/dosis/<string:peso>/<string:dosisT>")
def get_datosD(peso,dosisT):
    peso = float(peso)
    dosisT = float(dosisT)
    dosis = dosisT * peso
    return jsonify({"dosis" : dosis})


@app.route("/suspension/<string:dato1>/<string:mg>/<string:dosisT>/<string:ml>")
def get_DatosM(dato1, mg, dosisT, ml):
    peso1 = float(dato1)
    mg = float(mg)
    dosisT = float(dosisT)
    ml = float(ml)
    dosis = float(0)
    dosis = dosisT * peso1
    suspension = dosis * (ml/mg)
    return jsonify({"suspension" : suspension})



@app.route("/dosisDia/<string:dosisT>/<string:peso>/<string:horasM>")
def get_dosisDia(dosisT,peso,horasM):
    dosisT = float(dosisT)
    peso = float(peso)
    horasM = float(horasM)
    cc = float(0)
    cc = 24 / horasM
    dosisDia = (dosisT / cc)*100
    return jsonify({"dosisDia" : dosisDia, "cc":cc, "dosisT": dosisT


})



if __name__ == '__main__':
    app.run(debug=True, port=4000)
