from Monitoring_system.models import Webserver
from Monitoring_system import db


class WebserverService:
    def create_webserver(self,data):
        webserver = Webserver(name=data['name'], url=data['url'])
        db.session.add(webserver)
        db.session.commit()
        return {"message": "Webserver created"}

    def list_webservers(self):
        webservers = Webserver.query.all()
        return [{
           'id': ws.id,
           'name': ws.name,
           'url': ws.url,
        } for ws in webservers]


    def get_webserver(self,webserver_id):
        webserver = Webserver.query.get_or_404(webserver_id)
        return {
            'id': webserver.id,
            'name': webserver.name,
            'url': webserver.url,
        }


    def delete_webserver(self, webserver_id):
        webserver = Webserver.query.get_or_404(webserver_id)
        db.session.delete(webserver)
        db.session.commit()
        return {'message': 'Webserver deleted successfully'}, 200


    def update_webserver(self, webserver_id, data):
        webserver = Webserver.query.get_or_404(webserver_id)
        webserver.name = data['name']
        webserver.url = data['url']
        db.session.commit()
        return {'message': 'Webserver updated successfully'}