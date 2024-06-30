import requests
from threading import Timer
from datetime import datetime
from Monitoring_system.models import Webserver, Request
from Monitoring_system import db
from Monitoring_system.services import WebserverService

webserver_service = WebserverService()


def monitor_webservers():
    webservers = Webserver.query.all()
    for webserver in webservers:
        try:
            response = requests.get(webserver.url, timeout=60)
            latency = response.elapsed.total_seconds()
            success = response.status_code // 100 == 2 and latency < 60
            status = 'Healthy' if success else 'Unhealthy'

            new_request = Request(id=webserver.id, status_code=response.status_code, latency=latency)
            db.session.add(new_request)
            db.session.commit()

            webserver.status = 'Healthy' if check_health(webserver.id) else 'Unhealthy'
            webserver.last_checked = datetime.utcnow()
            db.session.commit()
        except requests.RequestException:
            new_request = Request(id=webserver.id, status_code=0, latency=60)  # failed request
            db.session.add(new_request)
            db.session.commit()
            webserver.status = 'Unhealthy'
            webserver.last_checked = datetime.utcnow()
            db.session.commit()

    Timer(60, monitor_webservers).start()


def check_health(webserver_id):
    requests = Request.query.filter_by(id=webserver_id).order_by(Request.timestamp.desc()).limit(5).all()
    success_count = sum(r.status_code // 100 == 2 and r.latency < 60 for r in requests)
    if success_count == 5:
        return True
    fail_count = sum(r.status_code // 100 != 2 or r.latency >= 60 for r in requests)
    return fail_count < 3
