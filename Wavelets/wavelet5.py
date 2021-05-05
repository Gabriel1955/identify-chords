import pywt
import numpy as np
import matplotlib.pyplot as plt

from scipy.signal import chirp

# Define signal
fs = 100
sampling_period = 1 / fs
t = np.linspace(0, 2, 2 * fs)
x = np.sin(2* np.pi *t * 10) +  np.sin(2* np.pi *t * 40) 

# Calculate continuous wavelet transform
coef, freqs = pywt.cwt(x, np.arange(1, fs), 'cgau1')
# for cof in coef:
# frequencies = pywt.scale2frequency('cmor1.5-1.0', np.arange(1, fs)) / sampling_perioda

# np.repeat(3, 4)
coef = abs(coef)
# print(len(frequencies))
# coef[9] = np.repeat(90, len(t))
# print(coef[20])?
# print(freqs)
# Show w.r.t. time and frequency
plt.pcolormesh(t, freqs*100, coef,shading='auto')
# plt.pcolor(np.linspace(0, 3, 3),np.linspace(0, 3, 3),[[1,0,0],[6,0,0],[20,0,0]],shading='auto')
# print(freqs)
# len(t) == len(coef[0]) and len(freqs) == len(coef)

# Set yscale, ylim and labels
plt.ylabel('Frequency (Hz)')
plt.xlabel('Time (sec)')
plt.show()
