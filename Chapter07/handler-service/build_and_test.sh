#!/bin/bash

cd app/
docker build -t ml-microservice:latest .
docker run -d -p 5000:5000 ml-microservice:latest
#curl http://localhost:5000/hello
#curl -d store_number=1 -d forecast_start_date="2021-10-01T00:00:00"
#docker ps
#curl 5000:5000/forecast -d store_number=1 -d forecast_start_date="2021-10-01T00:00:00"
