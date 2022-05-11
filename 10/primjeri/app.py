from flask import Flask,request,make_response,jsonify,render_template,url_for

app = Flask(__name__)

@app.route("/", methods=["GET"])
def home():
    return make_response(render_template("index.html"),200)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
