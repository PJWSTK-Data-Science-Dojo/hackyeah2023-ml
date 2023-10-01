FROM python:3.8-slim
WORKDIR /app
COPY . /app
EXPOSE 105
ENV FLASK_ENV=production
CMD ["./start.sh"]