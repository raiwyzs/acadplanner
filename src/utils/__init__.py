# Arquivo para guardar pedaços de código que são repetidos em vários lugares do projeto.

from models import engine, DataEvento, Relevancia, TipoEvento
from sqlalchemy import select, desc
from sqlalchemy.orm import Session

def get_relevancy_levels():
    with engine.connect() as conn:
        niveis_relevancia = conn.execute(
            select(Relevancia)
        ).scalars().all()
    return niveis_relevancia


def get_event_types():
    with engine.connect() as conn:
        tipo_eventos = conn.execute(
            select(TipoEvento)
        ).scalars().all()
    return tipo_eventos


def get_user_events(user_id):
    with engine.connect() as conn:
        datas = conn.execute(
            select(DataEvento).where(DataEvento.user_id == user_id).order_by(desc(DataEvento.data))
        ).scalars().all()
    return datas