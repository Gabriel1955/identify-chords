#https://medium.com/@cafelouco/usando-a-transformada-de-fourier-para-construir-um-visualizador-de-m%C3%BAsica-com-python-e-ardu%C3%ADno-57c98e723cdc
from numpy.core.fromnumeric import sort
from numpy.lib import median
from numpy.lib.arraypad import _round_if_needed
import pyaudio
import numpy as np
import time
from tkinter import TclError
import struct
from Music import identifyNote, getStringGuitarByFreq, getArrayChordByFreqs, MinDiffBetweenTwoNotesByFreq
from FrequencyMethods import getRealFrequency, getHarmonics
# from PlotGuitar import getNewPlot, updatePlot, addNote, show, printChordByArrayChord
# from PlotGuitar import plot
import csv
# f = open('dadosFrequencias1.csv', 'w', newline='', encoding='utf-8')
# w = csv.writer(f)
# w.writerow(["Freq","size","media","max_fft","min_freq","max_freq","Freq-min","max-Freq","left","right","OK"])


def classify(size,max):
  if max > 1300:
    return 1
  if max < 500:
    return 0
  return -1
  # if size > 8:
  #   return True
  # if size < 3:
  #   return False
  # if max < 500:
  #   return False
  

def top(input_list,N):
  input_list = sorted(input_list, reverse=True)
  return input_list[:N]
def getById(array, id):
  return array[id]
def txV(array):
  count = 0
  tx = []
  while count < len(array)-1:
    val = array[count+1]-array[count]
    tx.append(val*100/array[count])
    count = count + 1
  return tx

time.sleep(1)
np.set_printoptions(suppress=True) # don't use scientific notation

CHUNK = 1024 # number of data points to read at a time
RATE = 2000 # time resolution of the recording device (Hz)
WIDTH = 2

p=pyaudio.PyAudio() # start the PyAudio class
stream=p.open(format=p.get_format_from_width(WIDTH),channels=2,rate=RATE,input=True,
              frames_per_buffer=CHUNK) #uses default input 

# ax = getNewPlot()              
tx = 1.6
size = 60
contador = 0
maxi = 0
mini = 10000000

maxmedia = 0
minmedia =10000000
while True:   
  data = np.fromstring(stream.read(CHUNK),dtype=np.int16)
  data = data * np.hanning(len(data)) # smooth the FFT by windowing data
  fft = abs(np.fft.fft(data).real)
  fft = fft[:int(len(fft)/2)] # keep only first half
  freq = np.fft.fftfreq(CHUNK,1.0/RATE)
  freq = freq[:int(len(freq)/2)] # keep only first half
  if maxi < max(fft):
    maxi = max(fft)
  if mini >min(fft):
    mini = min(fft)

  media = np.median(fft) 

  if maxmedia < media:
    maxmedia = media
  if minmedia > media:
    minmedia = media
  # print(maxi)
  # print(mini)
  # print(maxmedia)
  # print(minmedia)
  # print(media)
  # print('--------')
  # E5 = 1
  # limitFFT = tx * media
  
  # print(freq)
  # print(fft[210])
  fft = fft[np.where(freq>=80)]
  freq = freq[np.where(freq>=80)]

  # freq = freq[np.where(fft>=75)]
  # fft = fft[np.where(fft>=75)]
  # print(freq)
  # print(fft)
  # print(np.median(freq))
  # print(len(freq))
  # print(getRealFrequency(freq,fft))
  # print("______________________________________________________")

  count = 0
  peaks = []
  NOTES_CHORD = []
  # # print(len(fft))
  while len(NOTES_CHORD) < 3 and len(freq) > 0:
    # print("Tem nota")
  #   # print(count)
  #   # media_old = np.median(fft)
  #   # print(media_old)
    id = np.where(fft == max(fft))
    
    peak = freq[id][0]
    peakfft = fft[id][0]
    
    NOTE_FREQ = identifyNote(peak)
    FREQ = peak
    diff = MinDiffBetweenTwoNotesByFreq(FREQ)/2
    where_extremos = (np.where((freq > FREQ+diff) | (freq < FREQ-diff)))
    where_meio = (np.where( (freq < FREQ+diff) & (freq > FREQ-diff) ))
    # print((peak,peakfft,id[0]))
    # fft_analizer = fft[where_meio]
    # freq_analizer = freq[where_meio]
    # if len(freq_analizer) > 0:
  #     if classify(len(freq_analizer),max(fft_analizer)) == 1:
      
    
    try:
      NOTES_CHORD.index(NOTE_FREQ[0])
      print((NOTE_FREQ[0],"Ja inserido"))
    except ValueError:
      NOTES_CHORD.append(NOTE_FREQ[0])
      # NOTES_CHORD.append(NOTE_FREQ[1])
  #     # print(len(freq_analizer))
  #     # print(np.median(fft_analizer))
  #     # print(max(fft_analizer))
  #     # print(freq_analizer)
  #     # print(fft_analizer)
  #     ok = 0
  #     if int(FREQ) == 196 or int(FREQ) == 164 or int(FREQ) == 130:
  #       ok = 1
  #     left = -1
  #     right = -1
  #     if len(freq_analizer) > 2:
  #       # print(peak)
  #       # print(FREQ)
  #       # print(freq_analizer)
  #       # print("------")
  #       id = list(freq_analizer).index(peak)
  #       if id > 1:
  #         left = fft_analizer[id]-fft_analizer[id-1]
  #         right = fft_analizer[id+1]-fft_analizer[id] 
  #     # w.writerow([int(FREQ),len(freq_analizer),int(np.median(fft_analizer)), int(max(fft_analizer)), int(min(freq_analizer)), int(max(freq_analizer)), int(FREQ-min(freq_analizer)), int(max(freq_analizer)-FREQ),left,right,ok])

  #   # if FREQ != 449.0:
  #     # time.sleep(10)
    
    fft = fft[where_extremos]
    freq = freq[where_extremos]
  print(sorted(NOTES_CHORD))
  print("_____________________")
  #   # if len(freq) > 0:
  #     # peaks.append(peak)
  #     # NOTE_FREQ = identifyNote(peak)
  #     # FREQS_CHORD.append(NOTE_FREQ[1])
  #     # # print(np.median(fft)/media_old)
  #   count = count + 1
  #   # time.sleep(4)
  # # print(sorted(FREQS_CHORD))
  # arrayChord = getArrayChordByFreqs(FREQS_CHORD)
  # print(arrayChord)
  #     # print(arrayChord[len(arrayChord)-1])
  # print(sorted(FREQS_CHORD))
  # print(sorted(peaks))
  # print("fim")
  # print("&&&&")


  # size = len(fft)
  # print(size)
  # indexs = np.argpartition(fft, -size)[-size:]
  # indexs = sorted(indexs, key=lambda id: freq[id])
  # print(list(map(lambda id: freq[id],)
  # bigners_freq = list(map(lambda id: freq[id],indexs))
  # bigners_fft = list(map(lambda id: fft[id],indexs))
  # media = np.median(bigners_fft)
  # print(media)
  # print(bigners_fft)
  # print(bigners_freq)s
  # print("++++++++++++++++++++++++++++")
  # print(freq)
  # print(sorted(fft))
  # sortedFFT = sorted(fft)
  # txVal = txV(sortedFFT)
  # id = np.argpartition(txVal, -1)[-1:][0]
  # print(sortedFFT)
  # print("txVAL")
  # print(txVal)
  # print(id)
  # print(txVal[id])
  # print(sortedFFT[id])
  # print(sortedFFT[id+1])
  # limitFFT = 3000
  # freqsPeak = freq[np.where(fft>=limitFFT)]
  # fftsPeak = fft[np.where(fft>=limitFFT)]
  # print(freqsPeak)
  # media = media * tx
  # ids = np.where(bigners_fft> media)[0]
  # freqsPeak = list(map(lambda id: bigners_freq[id], ids)) 
  # fftsPeak = list(map(lambda id: bigners_fft[id], ids))
  # print("--------------")
  # print(sorted(fftsPeak))
  # # print(freqsPeak)

  # if(len(freqsPeak) > 0):
  #   # print(freqsPeak)
  #   # print(fftsPeak)
  #   # updatePlot(ax)
  #   Harmonics = getHarmonics(freqsPeak,fftsPeak) 
  #   # print(Harmonics)
  #   NOTES = []
  #   FREQS_CHORD = []
  #   for Harmonic in Harmonics:
  #     FREQS = Harmonic[0]
  #     AMPLS = Harmonic[1]
  #     FREQ_REAL = getRealFrequency(FREQS,AMPLS)
  #     # print(FREQ_REAL)
  #     NOTE = identifyNote(FREQ_REAL)
  #     FREQ = NOTE[1]
  #     NOTE = NOTE[0]
  #     NOTES.append(NOTE)
  #     FREQS_CHORD.append(FREQ)
  #   # print(FREQS_CHORD)
  #   contador = contador + 1
  #   if len(FREQS_CHORD) < 3:
  #     tx = ((tx / 1.1) + tx)/2
  #     # size = size + 1
  #     contador = 1
  #   if len(FREQS_CHORD) > 3:
  #     tx = ((tx * 1.1) + tx)/2
  #     # size = size -1
  #     contador = 1
  #   # print(tx)
  #   # print(contador)
  #   # print(size)
  #   if len(FREQS_CHORD) > 2:
      
  #     arrayChord = getArrayChordByFreqs(FREQS_CHORD)
  #     # print(arrayChord)
  #     # print(arrayChord[len(arrayChord)-1])
  #     # printChordByArrayChord(arrayChord,ax)
  #   print('______________________________________________________________')
    # show()
    # time.sleep(10000000)
stream.stop_stream()
stream.close()
p.terminate()

