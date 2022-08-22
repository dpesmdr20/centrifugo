FROM centrifugo/centrifugo

LABEL maintainer="dpesmdr"

COPY ./centrifugo.json /centrifugo/config.json
COPY ./scripts /scripts
EXPOSE 8000
