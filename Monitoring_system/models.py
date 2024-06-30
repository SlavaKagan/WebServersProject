from datetime import datetime

from Monitoring_system import db


class Webserver(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    url = db.Column(db.String(255), nullable=False)
    status = db.Column(db.String(20), nullable=True)
    requests = db.relationship('Request', backref='webserver', lazy=True)


class Request(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    webserver_id = db.Column(db.Integer, db.ForeignKey('webserver.id'), nullable=False)
    status_code = db.Column(db.Integer, nullable=False)
    latency = db.Column(db.Float, nullable=False)
    timestamp = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
