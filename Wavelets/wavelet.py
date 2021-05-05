import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import pywt

def plot_wavelet(time, signal, scales, 
                 waveletname = 'cmor', 
                 cmap = plt.cm.seismic, 
                 title = 'Wavelet Transform (Power Spectrum) of signal', 
                 ylabel = 'Frequency', 
                 xlabel = 'Time'):
    
  dt = time[1] - time[0]
  [coefficients, frequencies] = pywt.cwt(signal, scales, waveletname, dt)
  power = (abs(coefficients)) ** 2
  period = frequencies
  levels = [0.0625, 0.125, 0.25, 0.5, 1, 2, 4, 8]
  contourlevels = np.log2(levels)
  
  fig, ax = plt.subplots(figsize=(15, 10))
  im = ax.contourf(time, np.log2(period), np.log2(power), contourlevels, extend='both',cmap=cmap)
  
  ax.set_title(title, fontsize=20)
  ax.set_ylabel(ylabel, fontsize=18)
  ax.set_xlabel(xlabel, fontsize=18)
  
  yticks = 2**np.arange(np.ceil(np.log2(period.min())), np.ceil(np.log2(period.max())))
  ax.set_yticks(np.log2(yticks))
  ax.set_yticklabels(yticks)
  ax.invert_yaxis()
  ylim = ax.get_ylim()
  ax.set_ylim(ylim[0], -1)
  
  cbar_ax = fig.add_axes([0.95, 0.5, 0.03, 0.25])
  fig.colorbar(im, cax=cbar_ax, orientation="vertical")
  plt.show()

# Data for plotting
t = np.arange(0.0, 2.0, 0.01)
s = 1 + np.sin(2 * np.pi * t)

# fig, ax = plt.subplots()
# ax.plot(t, s)

# ax.set(xlabel='time (s)', ylabel='voltage (mV)',
#        title='About as simple as it gets, folks')
# ax.grid()

# plt.show()
scales = np.arange(1, 128)
plot_wavelet(t, s, scales)