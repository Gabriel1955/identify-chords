#https://medium.com/@cafelouco/usando-a-transformada-de-fourier-para-construir-um-visualizador-de-m%C3%BAsica-com-python-e-ardu%C3%ADno-57c98e723cdc
import pyaudio
import numpy as np
import time
from tkinter import TclError
import struct
from Music import identifyNote, getStringGuitarByFreq, getArrayChordByFreqs
from FrequencyMethods import getRealFrequency, getHarmonics
from PlotGuitar import getNewPlot, updatePlot, addNote, show, printChordByArrayChord
# from PlotGuitar import plot

time.sleep(1)
np.set_printoptions(suppress=True) # don't use scientific notation

CHUNK = 1024 # number of data points to read at a time
RATE = 2000 # time resolution of the recording device (Hz)
WIDTH = 2

p=pyaudio.PyAudio() # start the PyAudio class
stream=p.open(format=p.get_format_from_width(WIDTH),channels=1,rate=RATE,input=True,
              frames_per_buffer=CHUNK) #uses default input 

# ax = getNewPlot()              

while True:   
  data = np.fromstring(stream.read(CHUNK),dtype=np.int16)
  # data = data * np.hanning(len(data)) # smooth the FFT by windowing data
  fft = abs(np.fft.fft(data).real)
  fft = fft[:int(len(fft)/2)] # keep only first half
  freq = np.fft.fftfreq(CHUNK,1.0/RATE)
  freq = freq[:int(len(freq)/2)] # keep only first half
  
  E5 = 10000
  limitFFT = max([np.max(fft)*0.3, 3.0* E5])

  freqsPeak = freq[np.where(fft>=limitFFT)]
  fftsPeak = fft[np.where(fft>=limitFFT)]

  if(len(freqsPeak) > 0):
    # print(freqsPeak)
    # updatePlot(ax)
    Harmonics = getHarmonics(freqsPeak,fftsPeak) 
    NOTES = []
    FREQS_CHORD = []
    for Harmonic in Harmonics:
      FREQS = Harmonic[0]
      AMPLS = Harmonic[1]
      FREQ_REAL = getRealFrequency(FREQS,AMPLS)
      NOTE = identifyNote(FREQ_REAL)
      FREQ = NOTE[1]
      NOTE = NOTE[0]
      NOTES.append(NOTE)
      FREQS_CHORD.append(FREQ)
    if len(FREQS_CHORD) > 2:
      # print(FREQS_CHORD)
      arrayChord = getArrayChordByFreqs(FREQS_CHORD)
      # print(arrayChord)
      print(arrayChord[len(arrayChord)-1])
      # printChordByArrayChord(arrayChord,ax)
    print('______________________________________________________________')
    # show()
stream.stop_stream()
stream.close()
p.terminate()

