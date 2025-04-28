#ederwander
import pyaudio 
from waves import sine_wave
import numpy as np
import wave
import cv2

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

freq = 1000

sin = sine_wave(frequency=freq)
while(True): 
    data = [next(sin) for i in range(chunk)]
    bytes = np.array(data).astype(np.float32).tobytes()
    stream.write(bytes) 

stream.stop_stream() 
stream.close() 
p.terminate() 

print()