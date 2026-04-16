from flask import Flask, jsonify, request

app = Flask(__name__)

def add_numbers(a, b):
    return a + b

@app.route("/")
def home():
    return """
    <h2>Add Two Numbers</h2>
    <form action="/add" method="get">
        <input type="number" name="a" placeholder="Enter first number" required><br><br>
        <input type="number" name="b" placeholder="Enter second number" required><br><br>
        <button type="submit">Calculate</button>
    </form>
    """

@app.route("/add")
def add():
    a = request.args.get("a", type=float)
    b = request.args.get("b", type=float)

    if a is None or b is None:
        return "Please enter two numbers"

    result = add_numbers(a, b)

    return f"""
    <h2>Result</h2>
    <p>{a} + {b} = {result}</p>
    <a href="/">Back</a>
    """

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
