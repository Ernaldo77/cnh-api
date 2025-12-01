from flask import Flask, request, jsonify, abort
from database import init_db
from model import (
    listar_carteiras,
    buscar_por_id,
    adicionar_carteira,
    atualizar_carteira,
    deletar_carteira,
    Carteira,
)

app = Flask(__name__)

initialized = False

@app.before_request
def inicializar_banco():
    init_db()
    initialized = True


@app.route("/")
def home():
    return("Bem vindo à Central de CNH API!")



@app.route("/nova", methods=["POST"])
def nova_carteira():
    dados = request.get_json() or {}

    nome = dados.get("nome")
    primeira_habilitacao = dados.get("primeira_habilitacao")
    data_nasc = dados.get("data_nasc")
    local_nasc = dados.get("local_nasc")
    UF_nasc = dados.get("UF_nasc")
    data_emissao = dados.get("data_emissao")
    validade = dados.get("validade")
    restricoes = dados.get("restricoes")
    doc_identidade = dados.get("doc_identidade")
    org_emissor = dados.get("org_emissor")
    UF_emissor = dados.get("UF_emissor")
    CPF = dados.get("CPF")
    n_registro = dados.get("n_registro")
    categoria = dados.get("categoria")
    nacionalidade = dados.get("nacionalidade")
    filiacao = dados.get("filiacao")
    observacoes = dados.get("observacoes")
    local = dados.get("local")

    carteira = adicionar_carteira(nome, primeira_habilitacao, data_nasc, local_nasc, UF_nasc, data_emissao, validade, restricoes, doc_identidade, org_emissor, UF_emissor, CPF, n_registro, categoria, nacionalidade, filiacao, observacoes, local)
    return jsonify(carteira.to_dict())

@app.route("/carteiras", methods=["GET"])
def listar():
    carteiras = listar_carteiras()
    return jsonify([t.to_dict() for t in carteiras]), 200


@app.route("/carteiraid/<int:id>", methods=["GET"])
def carteira_por_id(id):
    carteira = buscar_por_id(id)
    if not carteira:
        abort(404, mensagem="Carteira não encontrada.")
    return jsonify(carteira.to_dict()), 200


@app.route("/atualizar/<int:id>", methods=["PUT"])
def atualiza(id):
    carteira = buscar_por_id(id)
    if not carteira:
        abort(404, mensagem="Carteira não encontrada.")

    dados = request.get_json() or {}

    for campo, valor in dados.items():
        setattr(carteira, campo, valor)

    carteira = atualizar_carteira(carteira)
    return jsonify(carteira.to_dict()), 200


@app.route("/deletar/<int:id>", methods=["DELETE"])
def deletar(id):
    ok = deletar_carteira(id)
    if not ok:
        abort(404, mensagem="Carteira não encontrada.")
    return jsonify({"mensagem": "Tarefa removida com sucesso."}), 200


if __name__ == "__main__":
    app.run(debug=True)
