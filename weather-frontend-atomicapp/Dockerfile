FROM projectatomic/atomicapp:dev

MAINTAINER Christoph Görn <goern@redhat.com>

ADD /nulecule /Dockerfile /application-entity/
ADD /artifacts /application-entity/artifacts

LABEL Rebuild docker build --rm --tag goern/weather-frontend-atomicapp .

