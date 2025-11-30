class Carteira:
    _id_counter = 1

    def __init__(self, nome, primeira_habilitacao, data_nasc, local_nasc, UF_nasc, data_emissao, validade, restricoes, doc_identidade, org_emissor, UF_emissor, CPF, n_registro, categoria, nacionalidade, filiacao, observacoes, local):
        self.id = Carteira._id_counter
        self.nome = nome
        self.primeira_habilitacao = primeira_habilitacao
        self.data_nasc = data_nasc
        self.local_nasc = local_nasc
        self.UF_nasc = UF_nasc
        self.data_emissao = data_emissao
        self.validade = validade
        self.restricoes = restricoes
        self.doc_identidade = doc_identidade
        self.org_emissor = org_emissor
        self.UF_emissor = UF_emissor
        self.CPF = CPF
        self.n_registro = n_registro
        self.categoria = categoria
        self.nacionalidade = nacionalidade
        self.filiacao = filiacao
        self.observacoes = observacoes
        self.local = local
        Carteira._id_counter += 1
    
    def to_dict(self):
        return {
            "id": self.id,
            "nome": self.nome,
            "primeira_habilitacao": self.primeira_habilitacao,
            "data_nasc": self.data_nasc,
            "local_nasc": self.local_nasc,
            "UF_nasc": self.UF_nasc,
            "data_emissao": self.data_emissao,
            "validade": self.validade,
            "restricoes": self.restricoes,
            "doc_identidade": self.doc_identidade,
            "org_emissor": self.org_emissor,
            "UF_emissor": self.UF_emissor,
            "CPF": self.CPF,
            "n_registro": self.n_registro,
            "categoria": self.categoria,
            "nacionalidade": self.nacionalidade,
            "filiacao": self.filiacao,
            "observacoes": self.observacoes,
            "local": self.local
        }

carteiras = []


def listar():
    if carteiras == []:
        return "Nenhuma carteira registrada"
    return [carteira.to_dict() for carteira in carteiras]

def adicionar(carteira: Carteira):
    carteiras.append(carteira)
    return carteira.to_dict()

def buscar_por_id(carteira_id):
    for carteira in carteiras:
        if carteira.id == carteira_id:
            return carteira
    return None

def atualizar(carteira_id,novo_CPF=None, novo_nome=None, nova_primeira_habilitacao=None, nova_data_nasc=None, novo_local_nasc=None, nova_UF_nasc=None, nova_data_emissao=None, nova_validade=None, nova_restrioes=None, novo_doc_identidade=None, novo_org_emissor=None, nova_UF_emissor=None, novo_n_registro=None, nova_categoria=None, nova_nacionalidade=None, nova_filiacao=None, novas_observacoes=None, novo_local=None):
    carteira = buscar_por_id(carteira_id)
    if carteira:
        if novo_CPF:
            carteira.CPF = novo_CPF
        if novo_nome:
            carteira.nome = novo_nome
        if nova_primeira_habilitacao:
            carteira.primeira_habilitacao = nova_primeira_habilitacao
        if nova_data_nasc:
            carteira.data_nasc = nova_data_nasc
        if novo_local_nasc:
            carteira.local_nasc = novo_local_nasc
        if nova_UF_nasc:
            carteira.UF_nasc = nova_UF_nasc
        if nova_data_emissao:
            carteira.data_emissao = nova_data_emissao
        if nova_validade:
            carteira.validade = nova_validade
        if nova_restrioes:
            carteira.restricoes = nova_restrioes
        if novo_doc_identidade:
            carteira.doc_identidade = novo_doc_identidade
        if novo_org_emissor:
            carteira.org_emissor = novo_org_emissor
        if nova_UF_emissor:
            carteira.UF_emissor = nova_UF_emissor
        if novo_n_registro:
            carteira.n_registro = novo_n_registro
        if nova_categoria:
            carteira.categoria = nova_categoria
        if nova_nacionalidade:
            carteira.nacionalidade = nova_nacionalidade
        if nova_filiacao:
            carteira.filiacao = nova_filiacao
        if novas_observacoes:
            carteira.observacoes = novas_observacoes
        if novo_local:
            carteira.local = novo_local
        return carteira.to_dict()
    return None

def deletar(carteira_id):
    carteira = buscar_por_id(carteira_id)
    if carteira:
        carteiras.remove(carteira)
        return carteira.to_dict()
    return None

 
