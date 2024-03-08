import requests

INFERENCE_URL = "http://127.0.0.1:5000/inference"

def send_request():
    response = requests.post(INFERENCE_URL)

    if response.status_code == 200:
        data = response.json()
        image_paths = data.get("image_paths")
        print(f"Output image path: {image_paths}")
    else:
        print(f"Error: {response.text}")
send_request()