import math

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

def identify8(freq):
  if freq < 16.352:
    return 0
  return round(math.log(round(freq/16.352),2))


def MinDiffBetweenTwoNotesByFreq(freq):
  octave = identify8(freq)
  freq0 = freq / 2 **(octave-1)
  # aproximação linear das diferenças entre cada frequencia em oitava zero
  # 0,0561*Freq0 + 0,001 = dif
  DiffFundamental = 0.0561*freq0 + 0.001
  return DiffFundamental * 2** (octave-1)

print(MinDiffBetweenTwoNotesByFreq(197))

def identifyNote(freq):
  notes0 = getNotes0()
  notesName= ["C","C#","D","D#","E","F","F#","G","G#","A","A#","B"]
  octave = identify8(freq)
  if octave == 0:
    return '0'
  dif = 1000
  indexResult = 0
  index = 0
  for note in notes0:
    note = note * 2**(octave -1)
    mult = freq/note
    multRound = round(mult)
    difMult = multRound - mult
    if(difMult < 0):
      difMult = difMult * (-1)
    if(difMult < dif):
      dif = difMult
      indexResult = index
    index = index +1

  return notesName[indexResult]
