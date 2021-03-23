import sounddevice as sd
import questions, notes, sound_generator

def simple_sine_interval_question(l_bound, u_bound, ambitus):
    first, second = questions.interval_question(l_bound, u_bound, ambitus) 
    first_note = notes.n_th_piano_key_freq(first)
    second_note = notes.n_th_piano_key_freq(second)
    first_sound = sound_generator.generate_simple_sine(first_note, 1)
    second_sound = sound_generator.generate_simple_sine(second_note, 1)

    sd.play(first_sound, 48000)
    sd.wait()
    sd.play(second_sound, 48000)
    sd.wait()

    return str(abs(first - second))