# https://dsp.stackexchange.com/questions/62612/plotting-a-scalogram-of-a-signals-continuous-wavelet-transform-cwt-in-python
def plot_wavelet(ax, time2, signal, scales, waveletname = 'cmor', 
                 cmap =plt.cm.seismic, title = '', ylabel = '', xlabel = ''):
  dt=time2
  coefficients, frequencies = pywt.cwt(signal, scales, waveletname, dt)

  power = (abs(coefficients)) ** 2
  period = frequencies
  levels = [0.015625,0.03125,0.0625, 0.125, 0.25, 0.5, 1]
  contourlevels = np.log2(levels) #original
  time=range(2048)

  im = ax.contourf(time, np.log2(period), np.log2(power), contourlevels, extend='both',cmap=cmap)


  ax.set_title(title, fontsize=20)
  ax.set_ylabel(ylabel, fontsize=18)
  ax.set_xlabel(xlabel, fontsize=18)
  yticks = 2**np.arange(np.ceil(np.log2(period.min())), np.ceil(np.log2(period.max())))    
  ax.set_yticks(np.log2(yticks)) #original
  ax.set_yticklabels(yticks) #original
  ax.invert_yaxis()
  ylim = ax.get_ylim()

  cbar_ax = fig.add_axes([0.95, 0.5, 0.03, 0.25])
  fig.colorbar(im, cax=cbar_ax, orientation="vertical")

  return yticks, ylim
