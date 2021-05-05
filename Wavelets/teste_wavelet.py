from scipy import signal
import matplotlib.pyplot as plt
import numpy as np
from scipy.fftpack import fft



N = 600
T = 1.0 / 800.0

# t = np.linspace(0, 10, 2000, endpoint=False)
# sig  = np.cos(2 * np.pi * 2 * t)
t = np.linspace(0.0, N*T, N)
sig = np.sin(50.0 * 2.0*np.pi*t) 
widths = np.arange(1, 31)
cwtmatr = signal.cwt(sig, signal.ricker, widths)
plt.imshow(cwtmatr, extent=[0, 1, 1, 31], cmap='PRGn', aspect='auto')
plt.show()




yf = fft(sig)
xf = np.linspace(0.0, 1.0/(2.0*T), N/2)
import matplotlib.pyplot as plt
plt.plot(xf, 2.0/N * np.abs(yf[0:N/2]))
plt.grid()
plt.show()