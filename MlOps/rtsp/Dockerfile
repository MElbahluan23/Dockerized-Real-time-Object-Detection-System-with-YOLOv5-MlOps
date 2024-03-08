FROM python:3.8

RUN apt-get update && apt-get install -y \
    ffmpeg \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app

COPY . /app/

RUN pip install opencv-python flask requests pandas

EXPOSE 8080

CMD ["python", "rtsp.py"]
