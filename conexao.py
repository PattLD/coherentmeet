import sqlite3
from pathlib import Path

ROOT_PATH = Path(__file__).parent

conexao = sqlite3.connect(ROOT_PATH / "meu_banco.db")
cursor = conexao.cursor()

def criar_tabela(conexao,cursor): 
    cursor.execute("CREATE TABLE clientes (id INTEGER PRIMARY KEY AUTOINCREMENT, nome VARCHAR(100), email VARCHAR(150))")
    conexao.commit()

def inserir_registro(conexao, cursor, nome, email): 
    data = (nome, email)
    cursor.execute("INSERT INTO clientes (nome,email) VALUES (?,?)", data)
    conexao.commit()

def atualizar_registro(conexao,cursor,nome,email,id):
    data = (nome, email, id)
    cursor.execute("UPDATE clientes SET nome=?, email=? WHERE id=?;", data)
    conexao.commit()

def deletar_registo(conexao, cursor, id):
    data = (id,)
    cursor.execute("DELETE FROM clientes WHERE id=?", data)
    conexao.commit()

def inserir_em_lote(conexao,cursor,dados):
    cursor.executemany("INSERT INTO clientes (nome, email) VALUES (?,?)", dados)
    conexao.commit()

dados = [
    ("Alice Martins", "alice.martins@email.com"),
    ("Bruno Costa", "bruno.costa@email.com"),
    ("Camila Rocha", "camila.rocha@email.com"),
    ("Diego Fernandes", "diego.fernandes@email.com"),
    ("Elisa Gomes", "elisa.gomes@email.com"),
    ("Fernando Alves", "fernando.alves@email.com"),
    ("Gabriela Silva", "gabriela.silva@email.com"),
    ("Henrique Lima", "henrique.lima@email.com"),
    ("Isadora Mendes", "isadora.mendes@email.com"),
    ("João Pedro Castro", "joao.castro@email.com"),
    ("Larissa Carvalho", "larissa.carvalho@email.com"),
    ("Marcelo Nogueira", "marcelo.nogueira@email.com"),
    ("Natália Ribeiro", "natalia.ribeiro@email.com"),
    ("Otávio Moraes", "otavio.moraes@email.com"),
    ("Paula Vieira", "paula.vieira@email.com"),
    ("Rafael Teixeira", "rafael.teixeira@email.com"),
    ("Sílvia Peixoto", "silvia.peixoto@email.com"),
    ("Tiago Barros", "tiago.barros@email.com"),
    ("Úrsula Farias", "ursula.farias@email.com"),
    ("Vinícius Monteiro", "vinicius.monteiro@email.com")
]


