# RTSP-YOLO-Inference-MLOps

This project implements a solution for real-time object detection using an RTSP stream and YOLOv5 model inference. It consists of two containers: one for streaming the video as an RTSP stream and another for performing inference using YOLOv5 and Flask.

## Setup and Installation

To run this project, you need to have Docker installed on your system. Follow these steps:

1. Clone this repository:
   ```
   git clone https://github.com/MElbahluan23/RTSP-YOLO-Inference-MLOps.git
   ```

2. Navigate to the `MlOps` folder:
   ```
   cd RTSP-YOLO-Inference-MLOps/MlOps
   ```

3. Build and run the Docker containers using Docker Compose:
   ```
   sudo docker-compose up --build -d
   ```

## Usage

After the containers are up and running, you can run the Python script `script.py` to send a request to the inference container and print the path of the output annotated image. Here's how to do it:

1. Make sure the containers are running:
   ```
   sudo docker ps
   ```

2. Run the Python script:
   ```
   python script.py
   ```

## Folder Structure

```
MlOps
├── inference
│   ├── Dockerfile
│   └── inference.py
├── rtsp
│   ├── Dockerfile
│   ├── people_commerce_shop.mp4
│   └── rtsp.py
├── docker-compose.yml
└── script.py
```

- **inference**: Contains files related to the inference Flask container.
- **rtsp**: Contains files related to the RTSP streaming container.
- **docker-compose.yml**: Defines the Docker services and their configurations.
- **script.py**: Python script to send requests to the inference container.
