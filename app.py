from flask import Flask, request, jsonify
from flask_cors import CORS
from operaciones import operaciones

app = Flask(__name__)
CORS(app)


@app.route("/Index")
def realizaroperacion():

    if request.method == 'POST':

        result= {}
        val1=request.form.get('A')
        val2=request.form.get('B')

        sumar=suma(val1,val2)

        if sumar is not False:
            result["sumar"] = 1
            return result
        result["res"] = 0
        return result


        restar=resta(val1,val2)

        if restar is not False:
        	result["restar"]=2
        	return result	
        result["restar"]=0
        return result


        multi=multiplicar(val1,val2)

        if multi is not False:
        	result["multi"]=3
        	return result	
        result["restar"]=0
        return result

        divid=division(val)

        if divid is not False:
            result["division"]=4
            return result
        result["division"]=0
        return result






@app.route("/")
def index():
    return "Backend"


if __name__ == "__main__":
    app.run(threaded=True, port=5000, debug=True)
