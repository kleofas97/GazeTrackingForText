FROM python:3.8-slim

WORKDIR /app

COPY . .
RUN apt-get update && apt-get install -y build-essential cmake
RUN apt-get install ffmpeg libsm6 libxext6  -y
RUN pip install -U pip wheel cmake
RUN pip install -e .

EXPOSE 8000

CMD ["uvicorn", "src.api.endpoints:app", "--host", "0.0.0.0", "--port", "8000"]