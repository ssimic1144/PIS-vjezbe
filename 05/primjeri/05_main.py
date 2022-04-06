from flask import Flask, make_response, request, jsonify

app = Flask(__name__)

temp_storage = []

@app.route("/new/stuff", methods=["GET","POST"])
def new_stuff_function():
    if request.method == "POST":
        q_strings = request.args
        new_stuff = {}
        for key,value in q_strings.items():
            new_stuff[key]=value
        temp_storage.append(new_stuff)
        response = {"message":"Created"}
        return make_response(jsonify(response),201)
    else:
        response_list = []
        q_strings = request.args
        for key,value in q_strings.items():
            for item in temp_storage:
                if key in item:
                    if item[key] == value:
                        response_list.append(item)
        response = {"results":response_list}
        return make_response(jsonify(response), 200)


@app.route("/new/stuff/update", methods=["PATCH"])
def update_new_stuff_cost():
    json_request = request.json
    q_string = request.args
    for item in temp_storage:
        for key,value in item.items():
            if value == q_string["name"]:
                item["item"] = json_request["item"]
    response = {"response":"Updated"}
    return make_response(jsonify(response), 200)


@app.route("/delete/new/stuff", methods=["DELETE"])
def delete_stuff():
    q_string = request.args
    response = {"response":"Deleted"}
    good_response = make_response(jsonify(response), 200)
    for item in temp_storage:
        for key,value in item.items():
            if value == q_string["name"]:
                position = temp_storage.index(item)
                temp_storage.pop(position)
                return good_response
    response = {"response":"Name not found"}
    return make_response(jsonify(response), 400)

if __name__=="__main__":
    app.run(port=8080)
