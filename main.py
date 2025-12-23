import cv2
import time
from hand_detector import HandDetector
from gesture_map import get_gesture_text

cap = cv2.VideoCapture(0)
detector = HandDetector()

prev_gesture = ""
stable_count = 0
CONFIRM_FRAMES = 15   # adjust if needed

while True:
    success, img = cap.read()
    if not success:
        break

    img = detector.findHands(img)
    fingers = detector.fingersUp()
    gesture_text = get_gesture_text(fingers)

    # ----- STABILITY LOGIC -----
    if gesture_text == prev_gesture:
        stable_count += 1
    else:
        stable_count = 0
        prev_gesture = gesture_text

    # ----- DISPLAY TEXT -----
    cv2.putText(
        img, f"Gesture: {gesture_text}",
        (20, 50), cv2.FONT_HERSHEY_SIMPLEX,
        1, (0, 255, 0), 2
    )

    # ----- PROGRESS BAR -----
    bar_width = int((stable_count / CONFIRM_FRAMES) * 300)
    bar_width = min(bar_width, 300)

    cv2.rectangle(img, (20, 80), (320, 110), (255, 255, 255), 2)
    cv2.rectangle(img, (20, 80), (20 + bar_width, 110), (0, 255, 0), -1)

    # ----- CONFIRMED GESTURE -----
    if stable_count >= CONFIRM_FRAMES:
        cv2.putText(
            img, "CONFIRMED!",
            (20, 150), cv2.FONT_HERSHEY_SIMPLEX,
            1.2, (0, 0, 255), 3
        )

    cv2.imshow("HandSpeak", img)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()


