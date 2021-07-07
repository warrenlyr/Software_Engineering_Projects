# proj2-pageserver

A "getting started" manual for Dockers. CIS 322, Introduction to Software Engineering, at the University of Oregon. Reference: https://docs.docker.com/engine/reference/builder/

Author: Warren Liu

## Tasks

- The goal of this project is to implement the same "file checking" logic that you implemented in project 1 using flask.
- Like project 1, if a file ("name.html") exists, transmit "200/OK" header followed by that file html. If the file doesn't exist, transmit an error code in the header along with the appropriate page html in the body. You'll do this by creating error handlers taught in class (refer to the slides; it's got all the tricks needed). You'll also create the following two html files with the error messages.
  - "404.html" will display "File not found!"
  - "403.html" will display "File is forbidden!"
- Update your name and email in the Dockerfile.
- You will submit your credentials.ini in canvas. It should have information on how we should get your Dockerfile and your git repo.

## Use

```
docker build -t <name> .
docker run -d -p 5000:5000 <name>
```