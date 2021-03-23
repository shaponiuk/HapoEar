import sounddevice as sd
import numpy as np

def main():
    sr = 48000
    n_seconds = 3
    freq = 500
    step = 500 * np.pi * n_seconds / (sr * n_seconds)
    ar = np.arange(0, freq * np.pi, step)
    sound = np.sin(ar)
    sd.play(sound, sr)

if __name__ == '__main__':
    main()