# AI-Powered Integrated Emergency Response Drone

## 🚀 Project Overview
This AI-powered drone is designed for **swift delivery of medical aid, food, and rescue supplies** in disaster-hit regions. It uses **computer vision (YOLOv3)** for real-time **survivor detection**, **LiDAR-based obstacle avoidance**, and **GPS tracking** for autonomous navigation. The drone operates with **Pixhawk (ArduPilot), Raspberry Pi, and RPLIDAR A12**, demonstrating expertise in AI, robotics, and geospatial analysis.

## 🔹 Features
✅ **YOLOv3-based Object Detection** - Detects survivors & obstacles in real-time.  
✅ **LiDAR-based Navigation** - Avoids obstacles dynamically.  
✅ **GPS Tracking** - Sends survivor locations for quick rescue.  
✅ **Autonomous Flight Path Planning** - Uses ArduPilot & DroneKit for self-navigation.  
✅ **Real-time Image Processing** - Runs AI models on Raspberry Pi for onboard processing.  

## 📌 Technologies Used
- **Programming Language:** Python 🐍
- **Computer Vision:** OpenCV, YOLOv3, TensorFlow
- **AI & Deep Learning:** PyTorch, TensorFlow
- **Drone Control:** Pixhawk 6C, ArduPilot, DroneKit
- **Navigation & Mapping:** LiDAR (RPLIDAR A12), GPS (M8N), QGIS
- **Hardware:** Raspberry Pi, Pixhawk, Camera Module

## 🛠️ Installation
1️⃣ **Clone this repository:**
```bash
https://github.com/Ishwarihelgand/Integrated-Emergency-Response-Drone.git
```
2️⃣ **Install dependencies:**
```bash
pip install opencv-python numpy torch torchvision dronekit
```
3️⃣ **Download YOLOv3 Weights:**  
Download `yolov3.weights` from [YOLO Official Website](https://pjreddie.com/media/files/yolov3.weights) and place it in the project folder.

## 🚀 How to Run
Run the AI-powered drone script:
```bash
python drone_project.py
```
🔹 **Press 'q'** to exit the video stream.

## 📌 Expected Output
- If a **survivor is detected**, it prints:
  ```
  🚨 Survivor Detected! Sending GPS Location...
  📍 GPS Coordinates: 18.5236, 73.8478
  ```
- If an **obstacle is detected**, it prints:
  ```
  ⚠️ Obstacle Detected! Adjusting Flight Path...
  ```

## 💡 Future Improvements
✅ **Improve obstacle avoidance with Deep Reinforcement Learning**
✅ **Enhance real-time decision-making with cloud-based AI**
✅ **Integrate 5G communication for faster data transmission**

## 📄 License
This project is licensed under the **MIT License**.

---
📌 **Developed by:** *[Ishwari Helgand]* 🚀  

🔗 **GitHub:** https://github.com/Ishwarihelgand 

✉️ **Contact:** ishuhelgand@gmail.com










