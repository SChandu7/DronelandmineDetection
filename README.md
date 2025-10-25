# 🚁 Landmine Detection using Drone Camera

**Landmine Detection using Drone Camera** is an AI-powered drone project designed to enhance safety in mine-affected areas. The system uses a drone equipped with a camera and computer vision algorithms to detect landmines in real-time, allowing operators to safely monitor and avoid hazardous zones.

---

## ✨ Features

- 🚀 **Autonomous Drone Navigation** – Drone can fly over a designated area while capturing video for analysis.  
- 🎯 **Landmine Detection** – Uses AI and computer vision to identify landmines from camera feed.  
- 📹 **Real-time Monitoring** – Provides instant alerts to operators when potential landmines are detected.  
- 🗺️ **Mapping & Reporting** – Generates maps and reports of detected landmines for further analysis.  
- ⚠️ **Safety Enhancement** – Reduces human exposure to minefields and hazardous areas.  

---

## 🛠️ Technology Stack

- **Hardware:** Drone (custom-built or commercial), Camera module, ESP32/Raspberry Pi (for processing).  
- **Software:** Python, OpenCV, TensorFlow/Keras, Drone control APIs.  
- **AI Model:** Object detection model trained on landmine datasets.  
- **Data Handling:** Live video streaming and detection overlays.  

---

## 🚀 Getting Started

### Prerequisites

- Python 3.x  
- OpenCV, TensorFlow/Keras  
- Drone SDK or API access (e.g., DJI SDK, Tello, or custom drone)  
- Pretrained landmine detection model (or custom dataset)  

### Installation

```bash
# Clone the repository
git clone https://github.com/yourusername/Landmine-Detection-Drone.git

# Navigate to project folder
cd Landmine-Detection-Drone

# Install required Python packages
pip install -r requirements.txt

# Run the main detection script
python detect_landmine.py

```

## 🛠️ Usage
- Connect the drone to your control system.
- Start the drone flight within the target area.
- The drone camera streams live video to the processing unit.
- AI model analyzes frames in real-time for landmine detection.
- Alerts are sent if a potential landmine is detected.
- Generate maps or logs for the detected mine locations.

---

## 📸 Screenshots / Demo

Detecting The Lanmines in the images and sedning the co-ordinates the ground station and neglecting the part wheer the landmine does'nt exist

<img width="961" height="716" alt="image" src="https://github.com/user-attachments/assets/594759d6-31b6-4537-b409-7ceb055b48ab" />

-   For Video Demo Purpose [Click here](https://youtu.be/qjFEzs3fINk?si=DG2DIZnND4rzJpb7)


---
## 🤝 Contributing
We welcome contributions to improve detection accuracy, drone autonomy, or UI features.

---

## 📄 License
This project is licensed under the MIT License. See the LICENSE(Licencse) file for details.

---
