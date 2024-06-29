from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)
app.config.from_object('Monitoring_system.config.Config')
db = SQLAlchemy(app)
db.create_all()
migrate = Migrate(app, db)


from Monitoring_system import routes, models

