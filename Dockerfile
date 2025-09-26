FROM python:3.12-slim
WORKDIR /app
COPY p1.py .
CMD ["python", "p1.py"]
