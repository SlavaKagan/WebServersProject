# BylithProject

## Contact
**Email:** slava.kagan.ht@gmail.com

## General info about the task
**GitHub repository:** https://github.com/SlavaKagan/BylithProject <br />
**Programming Language:** Python (3.7.3) version https://www.python.org/ <br />
**Framework:** Flask (2.2.5)-Building RESTful APIs https://flask.palletsprojects.com/en/latest/ <br />
Flask-Migrate (2.5.2), Flask-SQLAlchemy (2.5.1) <br/>
**Database:** (SQL)-Postgresql 16 - https://www.postgresql.org/ <br />
**Database Name:** health_monitoring <br />
**MONGODB_URI:** SQLALCHEMY_DATABASE_URI connection string saved in the config file <br />
**Database Tables:** webserver+requests <br />
**Testing Code:** Package "pytest" (7.4.4) testing in python and assertions  https://flask.palletsprojects.com/en/3.0.x/testing/ <br />

## Abstract
System that enable health monitoring of webservers in the cloud.

## How to Run?
py run.py

## Core Functionality
    1. Ability to add / edit / delete / list webservers
    2. Development of automated worker that will monitor the webservers status
        a. Each webserver should be sampled at least 1 time per minute
        b. Webserver success status is determined by two factors: (AND)
            i. Getting HTTP Response Code 2xx
            ii. HTTP Response Latency < 60 seconds
        c. Every monitor request should be saved in a dedicated requests table for later use (History)
        d. Server is defined as “Healthy” in case 5 consecutive requests are considered “Success” as defined above
        e. Server is defined as “Unhealthy” in case 3 consecutive requests aren’t considered “Success” as defined above
    3. Development of a REST API including the following endpoints:
        a. Create Webserver – Endpoint that will allow creating a new Web Server
        b. Read (Get) Webserver – Should include all basic webserver details, current health status and last 10 requests objects
        c. Update Webserver – Endpoint that will allow updating Web Server
        d. Delete Webserver – Endpoint that will allow deleting Web Server
        e. Get list of all Web Servers and their current health-status
        f. Get list of a specific webserver requests history