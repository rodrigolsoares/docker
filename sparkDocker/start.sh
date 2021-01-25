#!/bin/bash
docker build -t spark-base docker/spark/spark-base && \
docker-compose up -d --build
