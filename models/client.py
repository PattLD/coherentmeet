import sqlalchemy as sa
from database import metadata

clients = sa.Table(
    "clients", 
    metadata, 
    sa.Column("id", sa.Integer, primary_key=True),
    sa.Column("name", sa.String(50), nullable=False),
    sa.Column("last_name", sa.String(150), nullable=False),
    sa.Column("cpf", sa.String(11), unique=True, nullable=False),
    sa.Column("email", sa.String(255), unique=True, nullable=False),
    sa.Column("birth_date", sa.Date, nullable=False),
    sa.Column("phone_number", sa.String(20), nullable=False),
    sa.Column("register_at", sa.DateTime(timezone=True), server_default=sa.func.now())
    ) 