from Monitoring_system import app
from Monitoring_system import worker

if __name__ == '__main__':
    worker.monitor_webservers()
    app.run(debug=True, port=5001)
