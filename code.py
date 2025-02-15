import cv2
import numpy as np
from dronekit import connect, VehicleMode, LocationGlobalRelative

# Connect to the drone (Use '127.0.0.1:14550' for simulation, or replace with real connection)
vehicle = connect('127.0.0.1:14550', wait_ready=True)

# Load YOLO Model
net = cv2.dnn.readNet("yolov3.weights", "yolov3.cfg")
layer_names = net.getLayerNames()
output_layers = [layer_names[i - 1] for i in net.getUnconnectedOutLayers()]
classes = open("coco.names").read().strip().split("\n")

def detect_survivors(frame):
    """Detects survivors using YOLOv3."""
    height, width = frame.shape[:2]
    blob = cv2.dnn.blobFromImage(frame, 0.00392, (416, 416), swapRB=True, crop=False)
    net.setInput(blob)
    outputs = net.forward(output_layers)

    for output in outputs:
        for detection in output:
            scores = detection[5:]
            class_id = np.argmax(scores)
            confidence = scores[class_id]

            if confidence > 0.5 and classes[class_id] == "person":
                print("🚨 Survivor Detected! Sending GPS Location...")
                latitude = vehicle.location.global_relative_frame.lat
                longitude = vehicle.location.global_relative_frame.lon
                print(f"📍 GPS Coordinates: {latitude}, {longitude}")

def check_obstacle():
    """Simulates LiDAR obstacle detection (Replace with real sensor data)."""
    import random
    distance = random.uniform(0.5, 5.0)  # Simulated obstacle distance
    if distance < 2.0:  # If an obstacle is too close
        print("⚠️ Obstacle Detected! Adjusting Flight Path...")
        vehicle.simple_goto(LocationGlobalRelative(vehicle.location.global_relative_frame.lat, 
                                                   vehicle.location.global_relative_frame.lon + 0.0001, 10))

def main():
    cap = cv2.VideoCapture(0)  # Open drone camera
    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break

        detect_survivors(frame)  # Detect survivors
        check_obstacle()  # Avoid obstacles

        cv2.imshow("Drone Camera", frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):  # Press 'q' to exit
            break

    cap.release()
    cv2.destroyAllWindows()
    vehicle.close()

if __name__ == "__main__":
    main()
