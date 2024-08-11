import sounddevice as sd
import numpy as np
import wavio

def record_audio(filename, duration, samplerate=44100):
    print("Recording...")
    # Record audio
    recording = sd.rec(int(duration * samplerate), samplerate=samplerate, channels=2, dtype='int16')
    sd.wait()  # Wait until the recording is finished
    print("Recording complete.")

    # Save the recording to a file
    wavio.write(filename, recording, samplerate, sampwidth=2)
    print(f"File saved as {filename}")

# Parameters
filename = 'output.wav'  # Output file name
duration = 10  # Duration of the recording in seconds

# Call the function
record_audio(filename, duration)
