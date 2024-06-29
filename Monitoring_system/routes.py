from flask import request, jsonify
from Monitoring_system import app, db
from Monitoring_system.models import Webserver
from Monitoring_system.services import WebserverService

webserver_service = WebserverService()


@app.route("/webservers", methods=['POST'])
def create_webserver():
    data = request.get_json()
    result = webserver_service.create_webserver(data)
    return jsonify(result), 201


@app.route('/webservers', methods=['GET'])
def list_webservers():
    result = webserver_service.list_webservers()
    return jsonify(result)


@app.route('/webservers/<int:id>', methods=['GET'])
def get_webserver(webserver_id):
    result = webserver_service.get_webserver(webserver_id)
    return jsonify(result)


@app.route('/webservers/<int:id>', methods=['DELETE'])
def delete_webserver(webserver_id):
    result = webserver_service.delete_webserver(webserver_id)
    return jsonify(result)


@app.route('/webservers/<int:id>', methods=['PUT'])
def update_webserver(webserver_id):
    data = request.get_json()
    result = webserver_service.update_webserver(webserver_id, data)
    return jsonify(result)
