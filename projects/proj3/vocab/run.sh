docker rm $(docker ps -a -q)
docker build -t flask-sample-one:latest .
docker run -d -p 5000:5000 flask-sample-one
