FROM centrifugo/centrifugo

LABEL maintainer="dpesmdr"

COPY ./centrifugo.json /centrifugo/config.json
EXPOSE 8000
