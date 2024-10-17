from sitePy import app, database # SITE PY VAI DAR PRPOBLEMA, RENOMEAR
from sitePy.models import Usuarios, foto
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.exc import SQLAlchemyError

try:
    with app.app_context(): # cria a database, deve rodar uma vez só
        database.create_all()
        print("great sucess")

    with app.app_context(): # cria um user teste
        user_instance = Usuarios(username='robson', passw='password123')
        database.session.add(user_instance)
        database.session.commit()
except SQLAlchemyError as e:
    print("erro : ", e)