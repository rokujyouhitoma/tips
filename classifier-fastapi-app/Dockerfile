# Builder
FROM python:3.12 as builder

RUN pip install fastapi uvicorn janome

# Runner
FROM python:3.12-slim

COPY --from=builder /usr/local/lib/python3.12/site-packages /usr/local/lib/python3.12/site-packages
COPY --from=builder /usr/local/bin/uvicorn /usr/local/bin/uvicorn

RUN useradd -r -s /bin/false uvicornusr

COPY ./app /app

USER uvicornusr

EXPOSE 8080

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8080"]
