#https://medium.com/@cafelouco/usando-a-transformada-de-fourier-para-construir-um-visualizador-de-m%C3%BAsica-com-python-e-ardu%C3%ADno-57c98e723cdc
import pyaudio
import numpy as np
import time
from tkinter import TclError
import struct
from Music import identifyNote

time.sleep(1)

np.set_printoptions(suppress=True) # don't use scientific notation

CHUNK = 40 # number of data points to read at a time
RATE = 44100 # time resolution of the recording device (Hz)

p=pyaudio.PyAudio() # start the PyAudio class
stream=p.open(format=pyaudio.paInt16,channels=1,rate=RATE,input=True,
              frames_per_buffer=CHUNK) #uses default input 
              
while True:   
  data = np.fromstring(stream.read(CHUNK),dtype=np.int16)
  data = data * np.hanning(len(data)) # smooth the FFT by windowing data
  fft = abs(np.fft.fft(data).real)
  fft = fft[:int(len(fft)/2)] # keep only first half
  freq = np.fft.fftfreq(CHUNK,1.0/RATE)
  freq = freq[:int(len(freq)/2)] # keep only first half
  # freqPeak = freq[np.where(fft==np.max(fft))[0][0]]+1
  # fftPeak = fft[np.where(fft==np.max(fft))[0][0]]

  freqsPeak = freq[np.where(fft>1000000)]
  fftspeak = fft[np.where(fft>1000000)]

  # print(freqsPeak)
  # print(np.max(fft))
  # print(round(fftPeak/10000))
  # print("peak frequency: %d Hz"%freqPeak)
  # if freqPeak > 16: 
  acordes= list(dict.fromkeys(map(identifyNote, sorted(freqsPeak))))
  if len(acordes) > 0:
    print(acordes)
    print(freqsPeak)
    print(fftspeak/100000)
    print("_________________")

  # for freqPeak in freqsPeak:
    # print(freqPeak)
    # print(identifyNote(freqPeak))
    #time.sleep(0.5)
  # time.sleep(0.3)



# close the stream gracefully
stream.stop_stream()
stream.close()
p.terminate()

