import cv2
import numpy as np
import os
import pyttsx3
import threading

# Initialize ORB and Matcher
orb = cv2.ORB_create(nfeatures=1000)
bf = cv2.BFMatcher(cv2.NORM_HAMMING)

# Text-to-Speech Engine
engine = pyttsx3.init()
engine.setProperty('rate', 150)  # speaking speed

# Use a separate thread to prevent freeze
def speak_alert(message):
    def run():
        engine.say(message)
        engine.runAndWait()
    threading.Thread(target=run, daemon=True).start()

# Load templates
template_folder = "templates"
templates = []

for filename in os.listdir(template_folder):
    if filename.lower().endswith(('.jpg', '.png', '.jpeg')):
        path = os.path.join(template_folder, filename)
        image = cv2.imread(path, 0)
        if image is not None:
            kp, des = orb.detectAndCompute(image, None)
            templates.append({'image': image, 'kp': kp, 'des': des, 'name': filename})
        else:
            print(f"Failed to load {filename}")

if not templates:
    print("No templates found.")
    exit()

# Open camera
cap = cv2.VideoCapture(0)
if not cap.isOpened():
    print("Cannot open camera")
    exit()

print("[INFO] Press 'q' to quit.")
landmine_alerted = False

while True:
    ret, frame = cap.read()
    if not ret:
        print("Frame error.")
        break

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    kp_frame, des_frame = orb.detectAndCompute(gray, None)

    if des_frame is None:
        cv2.imshow("Landmine Detection", frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
        continue

    landmine_detected = False

    for template in templates:
        matches = bf.knnMatch(template['des'], des_frame, k=2)

        # Apply Lowe's ratio test
        good_matches = []
        for m, n in matches:
            if m.distance < 0.75 * n.distance:
                good_matches.append(m)

        if len(good_matches) > 12:
            src_pts = np.float32([template['kp'][m.queryIdx].pt for m in good_matches]).reshape(-1, 1, 2)
            dst_pts = np.float32([kp_frame[m.trainIdx].pt for m in good_matches]).reshape(-1, 1, 2)

            M, mask = cv2.findHomography(src_pts, dst_pts, cv2.RANSAC, 5.0)

            if M is not None and mask is not None and mask.sum() > 10:
                h, w = template['image'].shape
                pts = np.float32([[0, 0], [0, h], [w, h], [w, 0]]).reshape(-1, 1, 2)
                dst = cv2.perspectiveTransform(pts, M)

                # Compute center
                center_x = int(np.mean(dst[:, 0, 0]))
                center_y = int(np.mean(dst[:, 0, 1]))

                # Draw circle
                cv2.circle(frame, (center_x, center_y), 50, (0, 255, 0), 2)

                # Draw label
                cv2.putText(frame, f"Alert: Landmine detected", (center_x - 60, center_y - 60),
                            cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 0, 255), 2)

                landmine_detected = True

    # Speak only once per detection
    if landmine_detected and not landmine_alerted:
        speak_alert("Landmine detected.")
        landmine_alerted = True
    elif not landmine_detected:
        landmine_alerted = False  # reset for next detection

    cv2.imshow("Landmine Detection", frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()