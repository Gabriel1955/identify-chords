#https://medium.com/@cafelouco/usando-a-transformada-de-fourier-para-construir-um-visualizador-de-m%C3%BAsica-com-python-e-ardu%C3%ADno-57c98e723cdc
import pyaudio
import numpy as np
from matplotlib.animation import FuncAnimation
from matplotlib import pyplot
import time
from tkinter import TclError
import struct
from Music import identifyNote
# import pycwt as wavelet


time.sleep(1)

figure = pyplot.figure()
line, = pyplot.plot_date([], [], '-')

np.set_printoptions(suppress=True) # don't use scientific notation

CHUNK = 4096 # number of data points to read at a time
RATE = 44100 # time resolution of the recording device (Hz)

p=pyaudio.PyAudio() # start the PyAudio class
stream=p.open(format=pyaudio.paInt16,channels=1,rate=RATE,input=True,
              frames_per_buffer=CHUNK) #uses default input 
              
def update(frame):   
  data = np.fromstring(stream.read(CHUNK),dtype=np.int16)
  data = data * np.hanning(len(data)) # smooth the FFT by windowing data
  fft = abs(np.fft.fft(data).real)
  fft = fft[:int(len(fft)/2)] # keep only first half
  freq = np.fft.fftfreq(CHUNK,1.0/RATE)
  freq = freq[:int(len(freq)/2)] # keep only first half
  freqPeak = freq[np.where(fft==np.max(fft))[0][0]]+1

  # num_steps = 10
  # x = np.arange(num_steps)
  # delta_t = x[1] - x[0]
  # scales = np.arange(1,num_steps+1)
  # freqs = 1/(wavelet.Morlet().flambda() * scales)
  # wavelet_type = 'morlet'

  # coefs, scales, freqs, coi, fft2, fftfreqs = wavelet.cwt(data, delta_t, wavelet=wavelet_type, freqs=freqs)

  # print("peak frequency: %d Hz"%freqPeak)
  # print(identifyNote(freqPeak))
  # freq = freq[np.where(fft>2000000)]
  # fft = fft[np.where(fft>2000000)]
  line.set_data(freq, fft)
  # line.set_data(coef)
  figure.gca().relim()
  figure.gca().autoscale_view()
  # time.sleep(0.5)
  return line, 

animation = FuncAnimation(figure, update, interval=20)

pyplot.show()

# uncomment this if you want to see what the freq vs FFT looks like
   
# close the stream gracefully
# stream.stop_stream()
# stream.close()
# p.terminate()
