FROM ubuntu:latest
LABEL authors="rupam"

ENTRYPOINT ["top", "-b"]