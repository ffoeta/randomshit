import math
from itertools import count

def sine_wave(frequency=440.0, framerate=44100, amplitude=0.5):
    period = int(framerate / frequency)
    if amplitude > 1.0: amplitude = 1.0
    if amplitude < 0.0: amplitude = 0.0
    lookup_table = [float(amplitude) * math.sin(2.0*math.pi*float(frequency)*(float(i%period)/float(framerate))) for i in range(period)]
    return (lookup_table[i%period] for i in count(0))

def white_noise(amplitude=0.5):
    return (float(amplitude) * math.random.uniform(-1, 1) for _ in count(0))