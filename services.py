import model as models
from model import Carteira

def listar_carteiras():
    return models.listar()

def listar_carteiras_por_id(id):
    return models.buscar_por_id(id)

def adicionar_carteira(dados):
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

    carteira = Carteira(
        nome=nome,
        primeira_habilitacao=primeira_habilitacao,
        data_nasc=data_nasc,
        local_nasc=local_nasc,
        UF_nasc=UF_nasc,
        data_emissao=data_emissao,
        validade=validade,
        restricoes=restricoes,
        doc_identidade=doc_identidade,
        org_emissor=org_emissor,
        UF_emissor=UF_emissor,
        CPF=CPF,
        n_registro=n_registro,
        categoria=categoria,
        nacionalidade=nacionalidade,
        filiacao=filiacao,
        observacoes=observacoes,
        local=local
    )
    return models.adicionar(carteira)

def atualizar_carteira(carteira_id, dados):
    if not models.buscar_por_id(carteira_id):
        raise IndexError("Carteira não encontrada")
    return models.atualizar(
        carteira_id,
        novo_CPF=dados.get("CPF"),
        novo_nome=dados.get("nome"),
        nova_primeira_habilitacao=dados.get("primeira_habilitacao"),
        nova_data_nasc=dados.get("data_nasc"),
        novo_local_nasc=dados.get("local_nasc"),
        nova_UF_nasc=dados.get("UF_nasc"),
        nova_data_emissao=dados.get("data_emissao"),
        nova_validade=dados.get("validade"),
        nova_restrioes=dados.get("restricoes"),
        novo_doc_identidade=dados.get("doc_identidade"),
        novo_org_emissor=dados.get("org_emissor"),
        nova_UF_emissor=dados.get("UF_emissor"),
        novo_n_registro=dados.get("n_registro"),
        nova_categoria=dados.get("categoria"),
        nova_nacionalidade=dados.get("nacionalidade"),
        nova_filiacao=dados.get("filiacao"),
        novas_observacoes=dados.get("observacoes"),
        novo_local=dados.get("local")
    )

def deletar_carteira(carteira_id):
    carteira_removida = models.deletar(carteira_id)
    if not carteira_removida:
        raise IndexError("Carteira não encontrada")
    return carteira_removida
