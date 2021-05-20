def shortestDistanceBetweenNotes(Freq):
  return Freq * 1.835/ 32.703

# def groupByDistance(Freqs):

def weightedAverage(Group):
  # print("Groups")
  # print(Group)
  sumAmpl = 0
  sumFreqXAmpl = 0
  for freq, ampl in Group:
    sumAmpl += ampl
    sumFreqXAmpl += freq * ampl
  return sumFreqXAmpl/sumAmpl, sumAmpl/len(Group)

def getPivots(Freqs, Ampls):
  # print("Pivolt")
  # print(Freqs)
  # print(Ampls)
  Group = []
  PivotsFreqs = []
  PivotsAmpls = []
  
  IndexPivot = 0
  AmplPivot = Ampls[0]
  FreqPivot = Freqs[0]
  Group.append((FreqPivot, AmplPivot))

  COUNT = 1
  SIZE_FREQS = len(Freqs)
  while COUNT < SIZE_FREQS:
    Freq = Freqs[COUNT]
    Ampl = Ampls[COUNT]
    if shortestDistanceBetweenNotes(FreqPivot)/1.4 > Freq - FreqPivot: #is between of limit
      if(AmplPivot <= Ampl):
        IndexPivot = COUNT
        AmplPivot = Ampl
        FreqPivot = Freq
    else:
      AverageFreq, AverageAmpl = weightedAverage(Group)
      PivotsFreqs.append(AverageFreq)
      PivotsAmpls.append(AverageAmpl)
      Group = []
      IndexPivot = COUNT
      AmplPivot = Ampl
      FreqPivot = Freq

    Group.append((Freq,Ampl))
    COUNT += 1

  AverageFreq, AverageAmpl = weightedAverage(Group)
  PivotsFreqs.append(AverageFreq)
  PivotsAmpls.append(AverageAmpl)
  
  return PivotsFreqs, PivotsAmpls



# Freqs = [430, 440, 450, 530, 545, 600]
# Ampls = [100, 120, 110, 90,  95,  100]
# Pivots = getPivots(Freqs, Ampls)
# print(Pivots)

