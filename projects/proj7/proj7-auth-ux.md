# Project 7: Adding authentication and user interface to brevet time calculator service

Author: Warren Liu

## Recap

You will reuse *your* code from project 6 (https://bitbucket.org/UOCIS322/proj6-rest/). Recall: you created the following three parts:

- You designed RESTful services to expose what is stored in MongoDB. Specifically, you used the boilerplate given in DockerRestAPI folder, and created the following:

** "http://<host:port>/listAll" should return all open and close times in the database

** "http://<host:port>/listOpenOnly" should return open times only

** "http://<host:port>/listCloseOnly" should return close times only

- You also designed two different representations: one in csv and one in json. For the above, JSON should be your default representation.

** "http://<host:port>/listAll/csv" should return all open and close times in CSV format

** "http://<host:port>/listOpenOnly/csv" should return open times only in CSV format

** "http://<host:port>/listCloseOnly/csv" should return close times only in CSV format

** "http://<host:port>/listAll/json" should return all open and close times in JSON format

** "http://<host:port>/listOpenOnly/json" should return open times only in JSON format

** "http://<host:port>/listCloseOnly/json" should return close times only in JSON format

- You also added a query parameter to get top "k" open and close times. For examples, see below.

** "http://<host:port>/listOpenOnly/csv?top=3" should return top 3 open times only (in ascending order) in CSV format

** "http://<host:port>/listOpenOnly/json?top=5" should return top 5 open times only (in ascending order) in JSON format

- You'll also designed consumer programs (e.g., in jQuery) to expose the services.

## Functionality you will add

In this project, you will add the following functionality:

### Part 1: Authenticating the services

- POST **/api/register**

Registers a new user. On success a status code 201 is returned. The body of the response contains a JSON object with the newly added user. A `Location` header contains the URI of the new user. On failure status code 400 (bad request) is returned. Note: The password is hashed before it is stored in the database. Once hashed, the original password is discarded. Your database should have three fields: id (unique index), username and password for storing the credentials.

- GET **/api/token**

Returns a token. This request must be authenticated using a HTTP Basic Authentication (see password.py for example). On success a JSON object is returned with a field `token` set to the authentication token for the user and a field `duration` set to the (approximate) number of seconds the token is valid. On failure status code 401 (unauthorized) is returned.

- GET **/RESOURCE-YOU-CREATED-IN-PROJECT-6**

Return a protected <resource>, which is basically what you created in project 6. This request must be authenticated using token-based authentication only (see testToken.py). HTTP password-based (basic) authentication is not allowed. On success a JSON object with data for the authenticated user is returned. On failure status code 401 (unauthorized) is returned.

### Part 2: User interface

The goal of this part of the project is to create frontend/UI for Brevet app using Flask-WTF and Flask-Login introduced in lectures. You frontend/UI should use the authentication that you created above. In addition to creating UI for basic authentication and token generation, you will add three additional functionalities in your UI: (a) remember me, (b) logout, and (c) CSRF protection. Note: You don’t have to maintain sessions.

## Tasks

You'll turn in your credentials.ini using which we will get the following:

- The working application with two parts.
- Dockerfile
- docker-compose.yml

## Ports

- Port 5000: ACP Calculator Api
- Port 5001: Login app

## Use

```
cd DockerRestAPI
```

\* have to cd DcolerRestAPI folder first * Then compose up

```
docker-compose up --build
```