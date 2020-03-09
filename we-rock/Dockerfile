FROM alpine

RUN apk add --upgrade apk-tools && apk add coreutils

RUN echo Will wait 5 seconds before quitting.

ENTRYPOINT ["/bin/sleep"]
CMD ["5"]
