# Dockerfile

# base image is python, the tag is 3.10.4-alpine3.14

FROM python:3.10.4-alpine3.14

COPY main.py main.py

EXPOSE 8080

CMD ["python", "main.py"]