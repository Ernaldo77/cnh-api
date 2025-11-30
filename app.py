from flask import Flask, request, jsonify
import services

app = Flask(__name__)


@app.route("/")
def home():
    return("Bem vindo à Central de CNH API!")

@app.route("/nova", methods=["POST"])
def nova_carteira():
    try:
        dados = request.get_json()
        mensagem_de_retorno = services.adicionar_carteira(dados)
        return jsonify(mensagem_de_retorno), 201
    except ValueError as e:
        return jsonify({"erro": str(e)}), 400

@app.route("/carteiras", methods=["GET"])
def listar():
    return jsonify(services.listar_carteiras())

@app.route("/atualizar/<int:id>", methods=["PUT"])
def atualizar(id):
    try:
        dados = request.get_json()
        carteira_atualizada = services.atualizar_carteira(id, dados)
        return jsonify(carteira_atualizada)
    except IndexError as e:
        return jsonify({"erro": str(e)}), 404

@app.route("/deletar/<int:id>", methods=["DELETE"])
def deletar(id):
    try:
        carteira = services.deletar_carteira(id)
        return jsonify({"mensagem": "Carteira removida com sucesso!", "carteira": carteira})
    except IndexError as e:
        return jsonify({"erro": str(e)}), 404

@app.route("/carteiraid/<int:id>", methods=["GET"])
def carteira_por_id(id):
    try:
        carteira = services.listar_carteiras_por_id(id)
        return jsonify(carteira.to_dict())
    except IndexError as e:
        return jsonify({"erro": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True)
