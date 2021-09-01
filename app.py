from logging import debug
from flask import Flask, render_template, request
import json


app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/hex")
def hex_view():
# conversion
    n = request.args.get("n")
    type_of_decode = request.args.get("type_of_decode")
    copy = n

    type_num = 16

    if type_of_decode == "hex":
        type_num = 16

    elif type_of_decode == "binary":
        type_num = 2

    elif type_of_decode == "Octal":
        type_num = 8

    elif type_of_decode == "Decimal":
        type_num = 10

    dec = int(n, type_num)
    res = "{0:08b}".format(int(n, type_num))
    onum = oct(int(n, type_num))  
    hex_value =  hex(int(n, type_num))     

    result = {
        "Hex Number" : hex_value,
        "Decimal Number" : dec,
        "Binary Number" : res,
        "Octal" : onum[2:]
    }

 

    return render_template("index.html", result=json.dumps(result))
 

if __name__ == "__main__":
    app.run(debug=True)