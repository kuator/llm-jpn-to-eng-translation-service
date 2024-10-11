FROM python:3.12.7-slim-bullseye

WORKDIR /app

COPY requirements.txt requirements.txt

RUN pip install --upgrade pip && pip install --no-cache-dir -Ur requirements.txt

EXPOSE 8001

COPY . .

CMD ["uvicorn", "src.main:app", "--host", "0.0.0.0", "--port", "8001"]
