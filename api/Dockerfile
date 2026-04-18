FROM alpine:3.20

RUN addgroup -S appgroup && adduser -S appuser -G appgroup \
    && apk add --no-cache python3 py3-pip redis \
    && pip install --break-system-packages flask redis

USER appuser
WORKDIR /app

CMD ["python3", "/app/api.py"]