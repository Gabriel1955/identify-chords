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