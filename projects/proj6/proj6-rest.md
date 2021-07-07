# Project 6: Brevet time calculator service

Simple listing service from project 5 stored in MongoDB database.

Author: Warren Liu

## Recap

You will reuse *your* code from project 5 (https://bitbucket.org/UOCIS322/proj5-mongo). Recall: you created the following functionalities. 1) Two buttons ("Submit") and ("Display") in the page where you have controle times. 2) On clicking the Submit button, the control times were be entered into the database. 3) On clicking the Display button, the entries from the database were be displayed in a new page. You also handled error cases appropriately.

## Functionality you will add

This project has following four parts. Change the values for host and port according to your machine, and use the web browser to check the results.

- You will design RESTful service to expose what is stored in MongoDB. Specifically, you'll use the boilerplate given in DockerRestAPI folder, and create the following three basic APIs:
  - "http://<host:port>/listAll" should return all open and close times in the database
  - "http://<host:port>/listOpenOnly" should return open times only
  - "http://<host:port>/listCloseOnly" should return close times only
- You will also design two different representations: one in csv and one in json. For the above, JSON should be your default representation for the above three basic APIs.
  - "http://<host:port>/listAll/csv" should return all open and close times in CSV format
  - "http://<host:port>/listOpenOnly/csv" should return open times only in CSV format
  - "http://<host:port>/listCloseOnly/csv" should return close times only in CSV format
  - "http://<host:port>/listAll/json" should return all open and close times in JSON format
  - "http://<host:port>/listOpenOnly/json" should return open times only in JSON format
  - "http://<host:port>/listCloseOnly/json" should return close times only in JSON format
- You will also add a query parameter to get top "k" open and close times. For examples, see below.
  - "http://<host:port>/listOpenOnly/csv?top=3" should return top 3 open times only (in ascending order) in CSV format
  - "http://<host:port>/listOpenOnly/json?top=5" should return top 5 open times only (in ascending order) in JSON format
  - "http://<host:port>/listCloseOnly/csv?top=6" should return top 5 close times only (in ascending order) in CSV format
  - "http://<host:port>/listCloseOnly/json?top=4" should return top 4 close times only (in ascending order) in JSON format
- You'll also design consumer programs (e.g., in jQuery) to use the service that you expose. "website" inside DockerRestAPI is an example of that. It is uses PHP. You're welcome to use either PHP or jQuery to consume your services. NOTE: your consumer program should be in a different container like example in DockerRestAPI.

## Tasks

You'll turn in your credentials.ini using which we will get the following:

- The working application with three parts.
- Dockerfile
- docker-compose.yml

## Use

```
docker-compose up --build
```