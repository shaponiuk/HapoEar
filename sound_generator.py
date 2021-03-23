import numpy as np
import random

def generate_simple_sine(freq, n_seconds, samplerate=48000, harmonics=None):
    n_samples = samplerate * n_seconds

    sound = np.zeros(n_samples)
    i = 1

    if harmonics == None:
        harmonics = rand_harmonics(17)

    for harmonic in harmonics:
        i_freq = freq * i
        last_val = i_freq * np.pi * n_seconds
        step = last_val / n_samples
        ar = np.arange(0, last_val, step)[:n_samples]
        scaled_sine = np.sin(ar) * harmonic
        sound += scaled_sine
        i += 1

    return sound

def rand_harmonics(n_harmonics):
    harmonics = []
    last_val = random.uniform(.7, .99)
    harmonics.append(last_val)

    for _ in range(n_harmonics - 1):
        last_val = random.uniform(last_val / 7, last_val * 2 / 3)
        harmonics.append(last_val)

    return harmonics
    