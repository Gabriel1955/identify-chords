import math
import time

def getStringGuitarByFreq(freq):
  C6 = 82.407
  C5 = 110
  C4 = 146.832
  C3 = 195.998
  C2 = 246.942
  C1 = 329.628
  if freq >= C6 and freq < C5:
    return 6
  elif freq >= C5 and freq < C4:
    return 5
  elif freq >= C4 and freq < C3:
    return 4
  elif freq >= C3 and freq < C2:
    return 3
  elif freq >= C2 and freq < C1:
    return 2
  elif freq >= C1 and freq < 444:
    return 1
  return 0


def getNotes0():
  C0 = 16.352
  Db0 = 17.324
  D0 = 18.354
  Eb0 = 19.445
  E0 = 20.602
  F0 = 21.827
  Gb0 = 23.125
  G0 = 24.500
  Ab0 = 25.957
  A0 = 27.500
  Bb0 = 29.135
  B0 = 30.868
  return  [C0,Db0,D0,Eb0,E0,F0,Gb0,G0,Ab0,A0,Bb0,B0]

def myRound(value):
  if (int(value) - value)**2 < (round(value) - value)**2:
    return int(value)
  return round(value)

def identify8(freq):
  if freq < 16.352:
    return 0
  # print(freq/16.352)
  # print(myRound(freq/16.352))
  # print(math.log(myRound(freq/16.352),2))
  # print(int(math.log(myRound(freq/16.352),2)))
  return int(math.log(int(freq/16.352),2))


def MinDiffBetweenTwoNotesByFreq(freq):
  octave = identify8(freq)
  freq0 = freq / 2 **(octave-1)
  # aproximação linear das diferenças entre cada frequencia em oitava zero
  # 0,0561*Freq0 + 0,001 = dif
  DiffFundamental = 0.0561*freq0 + 0.001
  return DiffFundamental * 2** (octave-1)

def identifyNote(freq):
  if freq < 33:
    return -1, -1
  notes0 = getNotes0()
  notesName= ["C","C#","D","D#","E","F","F#","G","G#","A","A#","B"]
  octave = identify8(freq)
  # print(octave)
  dif = 1000
  indexResult = 0
  FREQ = 0
  index = 0
  for note in notes0:
    note = note * 2**(octave)
    mult = freq/note
    multRound = round(mult)
    difMult = multRound - mult
    if(difMult < 0):
      difMult = difMult * (-1)
    if(difMult < dif):
      dif = difMult
      indexResult = index
      FREQ = note
    index = index +1
  NOTE = notesName[indexResult]
  return NOTE, FREQ

#identificar acordes
E2 = 82.408
G2 = 98
A2 = 110
B2 = 123.472
C3 = 130.816
D3 = 146.832
E3 = 164.816
G3 = 196
Ab3 = 207.656
A3 = 220
B3 = 246.944
C4 = 261.632
Db4 = 277.184
D4 = 293.664
E4 = 329.632
F4 = 349.232
Gb4 = 370
G4 = 392
A4 = 440
Chord_C =  [C3,E3,G3,C4,E4]
Chord_D =  [D3,A3,D4,Gb4]
Chord_E =  [E2,B2,E3,Ab3,B3,E4]
Chord_G =  [G2,B2,E3,G3,D4,G4]
Chord_A =  [A2,E3,A3,Db4,E4]
Chord_Am = [A2,E3,A3,C4,E4]
Chord_Em = [E2,B2,E3,G3,B3,E4]
Chord_Dm = [D3,A3,D4,F4]


Chords = [Chord_C, Chord_D,Chord_E,Chord_G,Chord_A,Chord_Am,Chord_Em, Chord_Dm]

def identifyChord(freqs):
  # print("identify")
  Percentage = 0
  chordIdentifed = [0]
  for chord0 in Chords:
    count = 0
    chord = chord0
    # print("chord 0")
    while count < 1:
      # print(chord)
      CurrentPercentage = getPercentageChord(freqs,chord)
      # print(CurrentPercentage)
      if CurrentPercentage > Percentage:
        Percentage = CurrentPercentage
        chordIdentifed = chord
        # print("new chord")
    # print(chordIdentifed)
      chord = nextChord(chord)
      count = count + 1
  return chordIdentifed

def getPercentageChord(freqs, chord):
  hits = 0
  for freq in freqs:
    # print(freq)
    try:
      chord.index(freq)
      hits = hits + 1
      # print("hit")
    except ValueError:
      # print("loss")
      continue
  return hits/len(chord)

def getNoteByFreq(freq):
  return identifyNote(freq)[0]

def getArrayChordByFreqs(freqs):
  # print(freqs)
  chord = identifyChord(freqs)
  # print(chord)
  return list(map(getNoteByFreq,chord))[::-1]


# print(getArrayChordByFreqs([130,196,220]))
# print(identifyNote(123.472))
# count = 120
# while count < 1000:
#   print(count)
#   print(identifyNote(count))
#   if identifyNote(count)[1]/count < 0.9:
#     time.sleep(2)
  # time.sleep(1)
  # count = count + 1

note0 = getNotes0()
def nextOctave(freq):
  return freq*2

def getFreqsNotes(octaves = 5):
  count = 0
  notes = getNotes0()
  notesCurrent = notes
  while count < octaves:
    notesCurrent = list(map(nextOctave, notesCurrent))
    notes = notes + notesCurrent
    count = count + 1
  return notes

FREQUENCIAS = getFreqsNotes()
def nextFreq(freq):
  if(freq < 1):
    return -2
  try:
    index = FREQUENCIAS.index(freq)
    return FREQUENCIAS[index+1]
  except ValueError:
    Note = identifyNote(freq)
    return nextFreq(Note[1])
def nextChord(chord):
  return list(map(nextFreq,chord))
# print(nextFreq(50))

# ch = identifyChord([110, 207, 330, 349])
# print("chord final")
# print(ch)
# getPercentageChord([58.27, 130.816, 164.816, 196.0, 329.632, 392.0, 659.264],Chord_C)
