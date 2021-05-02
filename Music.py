import math

def identify8(freq):
  if freq < 16.352:
    return 0
  return round(math.log(round(freq/16.352),2))


def identifyNote(freq):
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
  notesName= ["C","Db","D","Eb","E","F","Gb","G","Ab","A","Bb","B"]
  # notesName= ["C","D","E","F","G","A","B"]
  notes0 = [C0,Db0,D0,Eb0,E0,F0,Gb0,G0,Ab0,A0,Bb0,B0]
  # notes0 = [C0,D0,E0,F0,G0,A0,B0]
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
    # print(notesName[index])
    # print(note)
    # print(freq)
    # print(mult)
    # print(difMult)
    index = index +1


  return notesName[indexResult]

# print(identifyNote(3000))
