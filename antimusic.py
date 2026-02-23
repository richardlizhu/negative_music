import numpy as np
from scipy.io import wavfile

def generate_anti_noise(input_file, output_file):
    # Load the original sound file
    sample_rate, data = wavfile.read(input_file)

    # Invert the phase by multiplying by -1
    # This flips the waveform across the x-axis
    anti_noise = data * -1

    # Save the result as a new wav file
    # We use the same sample rate to ensure timing matches
    wavfile.write(output_file, sample_rate, anti_noise.astype(data.dtype))
    
    print(f"Anti-noise file generated: {output_file}")

# Usage
generate_anti_noise('test.wav', 'phase_inverted_sound.wav')