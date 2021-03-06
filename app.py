from flask import Flask, request, jsonify
from flask_cors import CORS
from operaciones import operaciones

app = Flask(__name__)
CORS(app)


@app.route("/Index",methods=['POST'])
def suma():
    global datos

    if request.method=='POST':
        return "Backend"
        valor1 = request.form.get('A')
        valor2 = request.form.get('B')
        sumar=sumarvalor(valor1,valor2)
        sumar=datos(request.json['numero1'],request.json['numero2'],request['operacion'])
        datos.append(sumar)

        restar=restavalor(valor1,valor2)
        restar=datos(request.json['numero1'],request.json['numero2'],request['operacion'])
        datos.append(restar)

        restar=restavalor(valor1,valor2)
        restar=datos(request.json['numero1'],request.json['numero2'],request['operacion'])
        datos.append(restar)

        multi=multiplicarvalor(valor1,valor2)
        multi=datos(request.json['numero1'],request.json['numero2'],request['operacion'])
        datos.append(multi)

@app.route("/Index",methods=['GET'])
def obtenerdatos():
    global op
    dato=[]
    respuesta={}
    for operaciones1 in op:
        datos={
            'a':operaciones.valor1,
            'b':datos.valor2,
            'resultado':datos.operacion
        }
        datos.append(datos)
    respuesta.jsonify(dato)
    return(respuesta)

@app.route("/")
def index():
    return "Backend"


if __name__ == "__main__":
    app.run(threaded=True, port=5000, debug=True)
