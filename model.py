from dataclasses import dataclass
from database import get_connection


@dataclass
class Carteira:
    id: int
    nome: str
    primeira_habilitacao: str
    data_nasc: str
    local_nasc: str
    UF_nasc: str
    data_emissao: str
    validade: str
    restricoes: str
    doc_identidade: str
    org_emissor: str
    UF_emissor: str
    CPF: str
    n_registro: str
    categoria: str
    nacionalidade: str
    filiacao: str
    observacoes: str
    local: str


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
            "local": self.local,
        }


def carteira_from_row(row):
    return Carteira(
        id=row["id"],
        nome=row["nome"],
        primeira_habilitacao=row["primeira_habilitacao"],
        data_nasc=row["data_nasc"],
        local_nasc=row["local_nasc"],
        UF_nasc=row["UF_nasc"],
        data_emissao=row["data_emissao"],
        validade=row["validade"],
        restricoes=row["restricoes"],
        doc_identidade=row["doc_identidade"],
        org_emissor=row["org_emissor"],
        UF_emissor=row["UF_emissor"],
        CPF=row["CPF"],
        n_registro=row["n_registro"],
        categoria=row["categoria"],
        nacionalidade=row["nacionalidade"],
        filiacao=row["filiacao"],
        observacoes=row["observacoes"],
        local=row["local"],
    )


def listar_carteiras():
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("SELECT * FROM carteiras")
    rows = cur.fetchall()
    conn.close()
    return [carteira_from_row(r) for r in rows]

def buscar_por_id(carteira_id):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("SELECT * FROM carteiras WHERE id = ?", (carteira_id,))
    row = cur.fetchone()
    conn.close()
    if row:
        return carteira_from_row(row)
    return None


def adicionar_carteira(nome, primeira_habilitacao, data_nasc, local_nasc, UF_nasc, data_emissao, validade, restricoes, doc_identidade, org_emissor, UF_emissor, CPF, n_registro, categoria, nacionalidade, filiacao, observacoes, local):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute(
        """
        INSERT INTO carteiras (nome, primeira_habilitacao, data_nasc, local_nasc, UF_nasc, data_emissao, validade, restricoes, doc_identidade, org_emissor, UF_emissor, CPF, n_registro, categoria, nacionalidade, filiacao, observacoes, local)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        """,
        (nome, primeira_habilitacao, data_nasc, local_nasc, UF_nasc, data_emissao, validade, restricoes, doc_identidade, org_emissor, UF_emissor, CPF, n_registro, categoria, nacionalidade, filiacao, observacoes, local)
    )
    conn.commit()
    id = cur.lastrowid
    conn.close()
    return buscar_por_id(id)


def atualizar_carteira(carteira):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute(
        """
        UPDATE carteiras
            SET nome = ?, primeira_habilitacao = ?, data_nasc = ?, local_nasc = ?, UF_nasc = ?, data_emissao = ?, validade = ?, restricoes = ?, doc_identidade = ?, org_emissor = ?, UF_emissor = ?, CPF = ?, n_registro = ?, categoria = ?, nacionalidade = ?, filiacao = ?, observacoes = ?, local = ?
        WHERE id = ?
        """,
        (carteira.nome, carteira.primeira_habilitacao, carteira.data_nasc, carteira.local_nasc, carteira.UF_nasc, carteira.data_emissao, carteira.validade, carteira.restricoes, carteira.doc_identidade, carteira.org_emissor, carteira.UF_emissor, carteira.CPF, carteira.n_registro, carteira.categoria, carteira.nacionalidade, carteira.filiacao, carteira.observacoes, carteira.local, carteira.id)
    )
    conn.commit()
    conn.close()
    return carteira


def deletar_carteira(carteira_id):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("DELETE FROM carteiras WHERE id = ?", (carteira_id,))
    conn.commit()
    deletou = cur.rowcount > 0
    conn.close()
    return deletou
 
