import numpy as np
import sounddevice as sd
from scipy.signal import butter, lfilter
import serial
import keyboard

# try:
ser = serial.Serial("COM3", 9600)
# except:
#     print("No device")
#     exit()
# Low-pass filter design

rcoff = 0.1
gcoff = 1
bcoff = 0.1

coffs = [rcoff, gcoff, bcoff]

rgb = [0, 0, 0]


def butter_lowpass(cutoff, fs, order=5):
    nyq = 0.5 * fs  # Nyquist Frequency
    normal_cutoff = cutoff / nyq
    b, a = butter(order, normal_cutoff, btype='low', analog=False)
    return b, a


def apply_lowpass_filter(data, b, a):
    return lfilter(b, a, data)

# Volume (RMS) calculation


def calculate_rms(audio_data):
    return np.sqrt(np.mean(audio_data**2))


# Parameters
fs = 48000  # Sample rate
cutoff = 250.0  # Cutoff frequency of the filter (Hz)
order = 6
chunk_size = 2048  # Number of samples per audio block

# Filter coefficients
b, a = butter_lowpass(cutoff, fs, order)

# Callback for audio stream


def audio_callback(indata, frames, time, status):
    if status:
        print(f"Status: {status}", flush=True)
    if keyboard.is_pressed("v"):
        print("V pressed")

    mono_data = indata[:, 0]  # Take first channel if stereo
    filtered_data = apply_lowpass_filter(mono_data, b, a)
    volume = calculate_rms(filtered_data)*100
    # print(f"Volume (filtered RMS): {volume:.4f}", flush=True)
    # print('*'*round(volume))
    volume = round(volume, 2)
    # print(volume)
    bass = (volume/20)*255
    # на 100 волюм е не повече от 50
    # print(bass)

    if bass < 123:
        bass = 0.01666*(bass**1.89)
    else:
        bass = 150 + 10*((bass-123)**0.5)
    bass = round(bass)
    if bass < 0:
        bass = 0
    elif bass > 255:
        bass = 255

    # bass = chr(bass)

    for c in range(0, 3):
        rgb[c] = round(bass * coffs[c])

    # print([0x01, 0x03, rgb[0], rgb[1], rgb[2], rgb[0] ^ rgb[1] ^ rgb[2]])
    ser.write(bytes([0x01, 0x03, rgb[0], rgb[1], rgb[2], rgb[0] ^ rgb[1] ^ rgb[2]]))
    ser.reset_input_buffer()
    # ser = serial.Serial("COM4", 9600)


# Start audio stream
with sd.InputStream(callback=audio_callback, channels=1, samplerate=fs, blocksize=chunk_size, device=3):
    print("Listening... Press Ctrl+C to stop.")
    try:
        while True:
            sd.sleep(1000)  # Sleep in milliseconds
    except KeyboardInterrupt:
        print("Stopped.")
