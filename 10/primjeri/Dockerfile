FROM python:3.9.12-slim-bullseye
WORKDIR app/
COPY requirements.txt req.txt
RUN pip3 install -r req.txt
COPY . .
CMD ["python3", "app.py"]

