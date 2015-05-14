FROM centos:7

MAINTAINER Christoph Görn <goern@redhat.com>

RUN echo -e "[epel]\nname=epel\nenabled=1\nbaseurl=https://dl.fedoraproject.org/pub/epel/7/x86_64/\ngpgcheck=0" > /etc/yum.repos.d/epel.repo

RUN yum install -y --setopt=tsflags=nodocs python-pip && \
    yum clean all

RUN pip install redis bottle

ADD server.py /server.py

CMD python /server.py
