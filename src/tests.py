from models import DataEvento, session

# oommit de teste

datas_eventos = session.query(DataEvento).all()
print(datas_eventos)