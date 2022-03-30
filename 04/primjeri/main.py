from flask import Flask,jsonify,make_response,request

app = Flask(__name__)

temp_storage = []

@app.route("/")
def home():
    response = {"message":"Hello World"}
    return make_response(jsonify(response), 200)

@app.route("/post/note",methods=["POST"])
def post_note():
    json_request = request.json
    temp_storage.append(json_request)
    response = {"message":"Created"}
    return make_response(jsonify(response),201)

@app.route("/get/notes", methods=["GET"])
def get_all_notes():
    response = {"res":temp_storage}
    return make_response(jsonify(response),200)

@app.route("/get/note", methods=["GET"])
def get_note_with_json():
    json_request = request.json
    response_list = []
    for item in temp_storage:
        for key,value in item.items():
            if json_request["cost"] == value:
                response_list.append(item)
    response = {"res":response_list}
    return make_response(jsonify(response), 200)

@app.route("/get/items/<item_type>", methods=["GET"])
def get_items_by_type(item_type):
    response_list = []
    for item in temp_storage:
        for key,_ in item.items():
            if key == item_type:
                response_list.append(item)
    response = {"res": response_list}
    return make_response(jsonify(response),200)

@app.route("/get/items/<item_type>/with", methods=["GET"])
def get_items_by_type_with_q_string(item_type):
    q_string = request.args.get("cost", type=int)
    response_list = []
    for item in temp_storage:
        if item_type in item:
            if q_string == item["cost"]:
                response_list.append(item)
    response = {"results":response_list}
    return make_response(jsonify(response), 200)

if __name__ == "__main__":
    app.run(port=8080)
