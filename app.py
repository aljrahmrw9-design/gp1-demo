from flask import Flask, jsonify, request

app = Flask(__name__)

def add_numbers(a, b):
    return a + b

@app.route("/")
def home():
    return jsonify({
        "status": "ok",
        "message": "Use /add?a=2&b=3 to add two numbers"
    })

@app.route("/add")
def add():
    a = request.args.get("a", type=float)
    b = request.args.get("b", type=float)

    if a is None or b is None:
        return jsonify({
            "status": "error",
            "message": "Please provide two numbers in the URL like /add?a=2&b=3"
        }), 400

    result = add_numbers(a, b)

    return jsonify({
        "status": "ok",
        "a": a,
        "b": b,
        "result": result
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
