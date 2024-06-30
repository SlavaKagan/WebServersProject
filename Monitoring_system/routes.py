from flask import request, jsonify
from Monitoring_system import app, db
from Monitoring_system.services import WebserverService, RequestService

webserver_service = WebserverService()
request_service = RequestService()


# Creating a new webserver
@app.route("/webservers", methods=['POST'])
def create_webserver():
    data = request.get_json()
    result = webserver_service.create_webserver(data)
    return jsonify(result), 201


# Get list of all Web Servers and their current health-status
@app.route('/webservers', methods=['GET'])
def get_list_webservers():
    result = webserver_service.get_list_webservers()
    return jsonify(result)


@app.route('/webservers/<int:webserver_id>', methods=['GET'])
def get_webserver(webserver_id):
    result = webserver_service.get_webserver(webserver_id)
    return jsonify(result)


@app.route('/webservers/<int:webserver_id>/requests', methods=['GET'])
def get_requests_history(webserver_id):
    result = request_service.get_requests_history(webserver_id)
    return jsonify(result)


# Updating a webserver
@app.route('/webservers/<int:webserver_id>', methods=['PUT'])
def update_webserver(webserver_id):
    data = request.get_json()
    result = webserver_service.update_webserver(webserver_id, data)
    return jsonify(result)


# Delete a webserver
@app.route('/webservers/<int:webserver_id>', methods=['DELETE'])
def delete_webserver(webserver_id):
    result = webserver_service.delete_webserver(webserver_id)
    return jsonify(result), 200
