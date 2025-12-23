import cv2
import mediapipe as mp

class HandDetector:
    def __init__(self):
        self.mpHands = mp.solutions.hands
        self.hands = self.mpHands.Hands(
            static_image_mode=False,
            max_num_hands=1,
            min_detection_confidence=0.7,
            min_tracking_confidence=0.7
        )
        self.mpDraw = mp.solutions.drawing_utils
        self.results = None

    def findHands(self, img):
        imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        self.results = self.hands.process(imgRGB)

        if self.results.multi_hand_landmarks:
            for handLms in self.results.multi_hand_landmarks:
                self.mpDraw.draw_landmarks(
                    img, handLms, self.mpHands.HAND_CONNECTIONS
                )
        return img

    def fingersUp(self):
        if not self.results or not self.results.multi_hand_landmarks:
            return [0,0,0,0,0]

        hand = self.results.multi_hand_landmarks[0]
        lm = hand.landmark

        fingers = []

        # Thumb
        fingers.append(1 if lm[4].x > lm[3].x else 0)

        # Other fingers
        tips = [8, 12, 16, 20]
        for tip in tips:
            fingers.append(1 if lm[tip].y < lm[tip-2].y else 0)

        return fingers
