from sitePy import app, database
from sitePy.models import user, foto

with app.app_context():
    database.create_all()