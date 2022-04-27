from pony import orm
from datetime import datetime
from flask import Flask,request,make_response,jsonify,render_template

DB = orm.Database()

app = Flask(__name__)

class Cijena(DB.Entity):
   cijena = orm.Required(float)
   datum = orm.Required(datetime)

DB.bind(provider="sqlite", filename="database.sqlite", create_db=True)
DB.generate_mapping(create_tables=True)

def add_price(json_request):
    try:
        cijena = json_request["cijena"]
        datum = json_request["datum"]
        with orm.db_session:
            Cijena(cijena=cijena,datum=datum)
            response = {"response":"Success"}
            return response
    except Exception as e:
        return {"response":"Fail","error":e}

def get_all_prices():
    try:
        with orm.db_session:
            db_querry = orm.select(x for x in Cijena)[:]
            results_list = []
            for r in db_querry:
                results_list.append(r.to_dict())
            response = {"response":"Success", "data":results_list}
            return response
    except Exception as e:
        return {"response":"Fail", "error":e}

@app.route("/api/add", methods=["POST"])
def api_add():
    try:
        json_request = request.json
    except Exception as e:
        response = {"response":e}
        return make_response(jsonify(response),400)

    response = add_price(json_request)

    if response["response"] == "Success":
        return make_response(jsonify(response),200)
    else:
        return make_response(jsonify(response),400)

@app.route("/", methods=["GET"])
def home():
    response = get_all_prices()
    api_data_cijena = [x["cijena"] for x in response["data"]]
    datumi = [str(x["datum"].date()) for x in response["data"]]
    if response["response"] == "Success":
        return make_response(render_template("index.html", y_axis=api_data_cijena ,x_axis=datumi),200)
    else:
        return make_response(jsonify(response),400)

if __name__ == "__main__":
    app.run(port=8080)
