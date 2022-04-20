from flask import Flask,request,make_response,jsonify, render_template, url_for, redirect
from pony import orm

DB = orm.Database()

app = Flask(__name__)

class Stvar(DB.Entity):
   stvar = orm.Required(str,unique=True)
   namjena = orm.Required(str)
   cijena = orm.Optional(float)

DB.bind(provider="sqlite", filename="database.sqlite", create_db=True)
DB.generate_mapping(create_tables=True)

def get_stvari():
    try:
        with orm.db_session:
            db_querry = orm.select(x for x in Stvar)[:]
            results_list = []
            for r in db_querry:
                results_list.append(r.to_dict())
            response = {"response":"Success", "data":results_list}
            return response
    except Exception as e:
        return {"response":"Fail", "error":str(e)}

def add_stvar(json_request):
    try:
        stvar = json_request["stvar"]
        namjena = json_request["namjena"]
        try:
            cijena = json_request["cijena"]
        except ValueError:
            cijena = None
        with orm.db_session:
            Stvar(stvar=stvar,namjena=namjena,cijena=cijena)
            response = {"response":"Success"}
            return response
    except Exception as e:
        return {"response":"Fail","error":str(e)}

@app.route("/stvar/dodaj", methods=["POST","GET"])
def dodaj_stvar():
    if request.method == "POST":
        try:
            json_request = {}
            for key,value in request.form.items():
                if value == "":
                    json_request[key] = None
                else:
                    json_request[key] = value
        except Exception as e:
            response = {"response":str(e)}
            return make_response(jsonify(response),400)

        response = add_stvar(json_request)

        if response["response"] == "Success":
            return make_response(render_template("dodaj.html"),200)
        else:
            return make_response(jsonify(response),400)
    else:
        return make_response(render_template("dodaj.html"),200)

@app.route("/stvar/vrati", methods=["GET"])
def vrati_stvar():
    response = get_stvari()
    if response["response"] == "Success":
        return make_response(render_template("vrati.html", data=response["data"]),200)
    else:
        return make_response(jsonify(response),400)

@app.route("/")
def home():
    return redirect(url_for("dodaj_stvar"))

if __name__ == "__main__":
    app.run(port=8080)
