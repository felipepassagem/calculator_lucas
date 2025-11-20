from flask import Flask, request, jsonify
from flask_cors import CORS
from .logic import calculate

app = Flask(__name__)
CORS(app)  # libera CORS para tudo (simples pro seu caso)

@app.route("/calc", methods=["POST"])
def calc():
    print(">>> /calc foi chamado")  # só pra você ver no console

    data = request.get_json()
    a = data.get("a")
    op = data.get("op")
    b = data.get("b")

    try:
        result = calculate(a, op, b)
        return jsonify({"result": result})
    except Exception as e:
        return jsonify({"error": str(e)}), 400

if __name__ == "__main__":
    app.run(debug=True, port=5000)