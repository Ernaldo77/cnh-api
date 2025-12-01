import sqlite3
from pathlib import Path

DB_PATH = Path("banco_de_carteiras")


def get_connection():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn


def init_db():
    conn = get_connection()
    cur = conn.cursor()
    cur.execute(
        """
        CREATE TABLE IF NOT EXISTS carteiras (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT,
            primeira_habilitacao TEXT,
            data_nasc TEXT,
            local_nasc TEXT,
            UF_nasc TEXT,
            data_emissao TEXT,
            validade TEXT,
            restricoes TEXT,
            doc_identidade TEXT,
            org_emissor TEXT,
            UF_emissor TEXT,
            CPF TEXT,
            n_registro TEXT,
            categoria TEXT,
            nacionalidade TEXT,
            filiacao TEXT,
            observacoes TEXT,
            local TEXT
        )
        """
    )
    conn.commit()
    conn.close()