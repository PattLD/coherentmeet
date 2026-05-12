import sqlalchemy as sa
from main import metadata

clients = sa.Table(
    "clients", 
    metadata, 
    sa.Column("id", sa.Integer, primary_key=True),
    sa.Column("nome", sa.String(50), nullable=False),
    sa.Column("sobrenome", sa.String(150), nullable=False),
    sa.Column("cpf", sa.String(11), unique=True, nullable=False),
    sa.Column("email", sa.String(255), unique=True, nullable=False),
    sa.Column("data_nascimento", sa.Date, nullable=False),
    sa.Column("telefone", sa.String(20), nullable=False),
    sa.Column("cadastro_em", sa.DateTime(timezone=True), server_default=sa.func.now())
    ) 