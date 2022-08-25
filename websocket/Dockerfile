FROM centrifugo/centrifugo:v3.0.5
LABEL maintainer="dpesmdr"

COPY ./centrifugo.json /centrifugo/config.json
COPY ./run.sh .

EXPOSE 9000
CMD sh run.sh
