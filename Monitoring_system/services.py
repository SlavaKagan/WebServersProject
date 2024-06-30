from Monitoring_system.models import Webserver, Request
from Monitoring_system import db, app


class WebserverService:
    @staticmethod
    def create_webserver(self,data):
        webserver = Webserver(name=data['name'], url=data['url'])
        db.session.add(webserver)
        db.session.commit()
        return {"message": "Webserver created"}

    @staticmethod
    def get_list_webservers(self):
        webservers = Webserver.query.all()
        return [{'id': w.id, 'name': w.name, 'url': w.url, 'status': w.status} for w in webservers]

    @staticmethod
    def get_webserver(self, webserver_id):
        webserver = Webserver.query.get_or_404(webserver_id)
        requests = Request.query.filter_by(id=webserver_id).order_by(Request.timestamp.desc()).limit(10).all()
        return {
            'id': webserver.id,
            'name': webserver.name,
            'url': webserver.url,
            'status': webserver.status,
            'requests': [{'status_code': r.status_code, 'latency': r.latency, 'timestamp': r.timestamp} for r in requests]
        }

    @staticmethod
    def update_webserver(self, webserver_id, data):
        webserver = Webserver.query.get_or_404(webserver_id)
        webserver.name = data['name']
        webserver.url = data['url']
        db.session.commit()
        return {'message': 'Webserver updated successfully'}

    @staticmethod
    def delete_webserver(self, webserver_id):
        webserver = Webserver.query.get_or_404(webserver_id)
        db.session.delete(webserver)
        db.session.commit()
        return {'message': 'Webserver deleted successfully'}


class RequestService:
    @staticmethod
    def get_requests_history(self, webserver_id):
        requests = Request.query.filter_by(id=webserver_id).order_by(Request.timestamp.desc()).all()
        return [{
            'status_code': r.status_code,
            'latency': r.latency,
            'timestamp': r.timestamp
        } for r in requests]
