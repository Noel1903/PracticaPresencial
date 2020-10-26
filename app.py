from flask import Flask, request, jsonify
from flask_cors import CORS
from operaciones import operaciones

app = Flask(__name__)
CORS(app)


@app.route("/Index",methods=['POST'])
def realizaroperacion():

    if request.method == 'GET':

        result= {}
        val1=request.form.get('A')
        val2=request.form.get('B')

        sumar=suma(val1,val2)

        restar=resta(val1,val2)

        multi=multiplicar(val1,val2)

        divid=division(val1,val2)


@app.route("/")
def index():
    return "Backend"


if __name__ == "__main__":
    app.run(threaded=True, port=5000, debug=True)
