from flask import Flask

app = Flask(__name__)


@app.route("/", methods=["GET"])
def root():
    return "MY python flask APP"

app.run(host="0.0.0.0", port=4000)