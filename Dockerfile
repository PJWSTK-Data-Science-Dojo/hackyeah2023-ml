FROM python:3.8-slim
WORKDIR /app
COPY . /app
EXPOSE 105
ENV FLASK_ENV=production

RUN pip install --upgrade pip && \
    pip install --trusted-host pypi.python.org -r requirements.txt

ENTRYPOINT ["python", "main.py"]