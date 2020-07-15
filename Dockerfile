FROM ubuntu:18.04


RUN apt-get upgrade
RUN apt-get update
# RUN echo "y" | apt-get install python3-pip
RUN apt-get -y install python3-pip
RUN pip3 install django
RUN pip3 install psycopg2-binary
RUN mkdir /src
WORKDIR /src