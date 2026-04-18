FROM alpine:3.20

RUN addgroup -S appgroup && adduser -S appuser -G appgroup \
    && apk add --no-cache curl nmap redis postgresql-client

USER appuser
WORKDIR /app

CMD ["sh", "-c", "sleep infinity"]