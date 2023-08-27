FROM centos:7

WORKDIR /opt/app

USER root
RUN yum install -y gcc python3 python36-devel mysql-devel
RUN pip3 install --upgrade pip
COPY ./src/server/requirements.txt /opt/app/
RUN pip3 install -r requirements.txt