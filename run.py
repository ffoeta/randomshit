from track_hands import get_hands_landmarks, diff_thumb_index, diff_thumb_middle
import cv2
import mediapipe as mp
import pyaudio
import sounddevice as sd
import numpy as np
import math
from waves import sine_wave

mp_hands = mp.solutions.hands

cap = cv2.VideoCapture(0)

def norm(x):
    return abs(x * 4)


chunk = 1024 
FORMAT = pyaudio.paInt16 
CHANNELS = 1 
RATE = 8800 
K=0 
DISTORTION = 0.61

p = pyaudio.PyAudio() 

stream = p.open(
    format = FORMAT, 
    channels = CHANNELS, 
    rate = RATE, 
    output = True, 
    frames_per_buffer = chunk
)


while True:
    ret, frame = cap.read()
    frame = cv2.flip(frame, 1)
    frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    x = 0
    y = 0
    hands_landmarks = get_hands_landmarks(frame)
    for i, hand_landmarks in hands_landmarks:
        x = diff_thumb_index(hand_landmarks)
        y = diff_thumb_middle(hand_landmarks)

        freq = 1000 + norm(x) * 2000
        amplitude = x

        print(freq)
        print(amplitude)
        
        sin = sine_wave(frequency=freq, amplitude=amplitude)
        data = [next(sin) for i in range(chunk)]
        bytes = np.array(data).astype(np.float32).tobytes()
        stream.write(bytes) 

    cv2.imshow('MediaPipe Hands', cv2.flip(frame, 1))
    
    key = cv2.waitKey(1) & 0xFF
    if key == ord('q'):
        break
    if key == ord('t'):
        print(x)

        

stream.stop_stream()
stream.close()
cap.release()
cv2.destroyAllWindows()