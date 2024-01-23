# simple hello world webserver; source:
# https://github.com/crccheck/docker-hello-world/blob/master/Dockerfile

FROM busybox:latest
ENV PORT=8000
LABEL maintainer="Chris <c@crccheck.com>"

ADD index.html /www/index.html

# EXPOSE $PORT

HEALTHCHECK CMD nc -z localhost $PORT

# Create a basic webserver and run it until the container is stopped
CMD echo "webapp started on:" && echo "http://0.0.0.0:80" && \
    trap "exit 0;" TERM INT; httpd -v -p $PORT -h /www -f & wait