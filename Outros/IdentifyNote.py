import math

def identify8(freq):
  if freq < 33:
    return -1
  return int(math.log(int(freq/33),2))


def identifyNote(freq):
  C0 = 0
  Db0 = 1.947
  D0 = 4.026
  Eb0 = 6.237
  E0 = 8.58
  F0 = 11.055
  Gb0 = 13.662
  G0 = 16.434
  Ab0 = 19.371
  A0 = 22.506
  Bb0 = 25.506
  B0 = 29.135
  notesName= ["C","Db","D","Eb","E","F","Gb","G","Ab","A","Bb","B"]
  notes0 = [C0,Db0,D0,Eb0,E0,F0,Gb0,G0,Ab0,A0,Bb0,B0]
  O = identify8(freq)
  if O == -1:
    return 0
  
  constNote = (freq - (2**O) * 33)/(2**O)

  return notesName[freqNote]
