import numpy as np 
import matplotlib.pyplot as plt 
import scipy.fftpack 
import pyaudio
import time


time.sleep(1)
np.set_printoptions(suppress=True) # don't use scientific notation

CHUNK = 1024 # number of data points to read at a time
RATE = 1000 # time resolution of the recording device (Hz)
WIDTH = 2

p=pyaudio.PyAudio() # start the PyAudio class
stream=p.open(format=p.get_format_from_width(WIDTH),channels=1,rate=RATE,input=True,
              frames_per_buffer=CHUNK) #uses default input 

# ax = getNewPlot()              
fig, ax = plt.subplots() 
count = 82
while True:   
  plt.ion()
  data = np.fromstring(stream.read(CHUNK),dtype=np.int16)
  data = data * np.hanning(len(data)) # smooth the FFT by windowing data
  # fft = abs(np.fft.fft(data).real)
  # fft = fft[:int(len(fft)/2)] # keep only first half
  # freq = np.fft.fftfreq(CHUNK,1.0/RATE)
  # freq = freq[:int(len(freq)/2)] # keep only first half
  # E5 = 00000
  # limitFFT = max([np.max(fft)*0.2, 3.0* E5])

  # freqsPeak = freq[np.where(fft>=limitFFT)]
  # fftsPeak = fft[np.where(fft>=limitFFT)]
  # N = 800 
# sample spacing 
  # T = 1.0 / 800.0 
  x = np.linspace(0.0, CHUNK/RATE, CHUNK) 
  y = np.sin(count * 2.0*np.pi*x) + np.sin(60 * 2.0*np.pi*x)+ np.sin(30 * 2.0*np.pi*x)
  yf = scipy.fftpack.fft(y) 
  xf = np.linspace(0.0, 1.0/(2.0*(1/RATE)), int(CHUNK/2)) 
  ax.plot(xf, 2.0/CHUNK * np.abs(yf[:CHUNK//2])) 
  plt.pause(1)
  ax.clear()
stream.stop_stream()
stream.close()
p.terminate()

