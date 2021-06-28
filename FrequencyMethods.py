from Music import MinDiffBetweenTwoNotesByFreq


def getRealFrequency(freqs, ampls):
    SIZE_FREQS = len(freqs)
    COUNT = 0
    SUM_Ampls = 0
    SUM_FreqsxAmpls = 0
    
    while COUNT< SIZE_FREQS:
        SUM_Ampls = SUM_Ampls + ampls[COUNT]
        SUM_FreqsxAmpls = SUM_FreqsxAmpls + freqs[COUNT]*ampls[COUNT]
        COUNT = COUNT + 1
    
    return SUM_FreqsxAmpls/SUM_Ampls 

def getHarmonics(freqs, ampls):
    Harmonics = []
    COUNT = 1
    SIZE_FREQS = len(freqs)
    BufferFreqs = [freqs[0]]
    BufferAmpls = [ampls[0]]
    while COUNT < SIZE_FREQS:
        DiffBetweenTwoHarmonics = MinDiffBetweenTwoNotesByFreq(freqs[COUNT])
        # print(freqs[COUNT])
        # print(freqs[COUNT-1])
        # print(DiffBetweenTwoHarmonics)
        # print("----------")
        if(abs(freqs[COUNT] - freqs[COUNT-1]) > DiffBetweenTwoHarmonics):
            # print("zerou")
            Harmonics.append((BufferFreqs,BufferAmpls))
            BufferFreqs = []
            BufferAmpls = []
        BufferFreqs.append(freqs[COUNT])
        BufferAmpls.append(ampls[COUNT])    
        COUNT = COUNT + 1
    Harmonics.append((BufferFreqs,BufferAmpls))
    return Harmonics

