from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# Página inicial
@app.route("/")
def home():
    return render_template("index.html")


# Rota da IA da Mentis
@app.route("/analisar", methods=["POST"])
def analisar():

    respostas = request.json

    print("Respostas recebidas:")
    print(respostas)

    return jsonify({
        "status": "sucesso",
        "mensagem": "Dados recebidos pela IA da Mentis"
    })


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)