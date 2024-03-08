import torch
import cv2
import requests
from flask import Flask, request, jsonify
from pathlib import Path


MODEL = "yolov5s"

RTSP_URL = "http://mlops_rtsp_1:8080/streaming"

model = torch.hub.load("ultralytics/yolov5", MODEL, pretrained=True)

app = Flask(__name__)


@app.route("/inference", methods=["POST"])
def inference():
    cap = cv2.VideoCapture(RTSP_URL)
    output_dir = 'detected_frames'
    Path(output_dir).mkdir(parents=True, exist_ok=True)

    frame_count = 0
    file_paths = []
    while cap.isOpened() and frame_count < 50:
        _, frame = cap.read()
        results = model(frame)

        for detection in results.xyxy[0]:
            if detection[5] == 0: 
                x1, y1, x2, y2, confidence = detection[:5].tolist()
                x1, y1, x2, y2 = int(x1), int(y1), int(x2), int(y2)
                cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)
        file_path = f'{output_dir}/frame_{frame_count}.jpg'
        cv2.imwrite(file_path, frame)
        file_paths.append(file_path)
        frame_count += 1

    cap.release()

    return jsonify({"image_paths": file_paths})

def run_app():
    print("inference Run")
    app.run(host='0.0.0.0', port=5000)

if __name__ == "__main__":
    run_app()
