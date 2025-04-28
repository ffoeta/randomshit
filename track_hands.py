import mediapipe as mp
import math

mp_hands = mp.solutions.hands
hands = mp_hands.Hands(min_detection_confidence=0.7, min_tracking_confidence=0.7, max_num_hands=2)
mp_drawing = mp.solutions.drawing_utils

def get_hands_landmarks(frame):
    hands_from_frame = hands.process(frame)

    if hands_from_frame.multi_hand_landmarks:
        results = []
        index = 0
        hands_landmarks = hands_from_frame.multi_hand_landmarks
        for hand_landmarks in hands_landmarks:
            if not hand_landmarks or len(hand_landmarks.landmark) < 21:
                continue
            mp_drawing.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)
            results.append((index, hand_landmarks))
            index += 1
        return results
    else:
        return []

def diff_thumb_index(hand_landmarks):
    return diff(hand_landmarks, mp_hands.HandLandmark.THUMB_TIP, mp_hands.HandLandmark.INDEX_FINGER_TIP)
        
def diff_thumb_middle(hand_landmarks):
    return diff(hand_landmarks, mp_hands.HandLandmark.THUMB_TIP, mp_hands.HandLandmark.MIDDLE_FINGER_TIP)

def diff(hand_landmarks, first_name, second_name):
    first =  hand_landmarks.landmark[first_name]
    second =  hand_landmarks.landmark[second_name]
    return math.sqrt((first.x - second.x)**2 + (first.y - second.y)**2 + (first.z - second.z)**2)
