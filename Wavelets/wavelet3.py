import pywt
import numpy as np
import matplotlib.pyplot as plt
x = np.arange(300)
y = np.sin(2*np.pi*x*90)
coef, freqs=pywt.cwt(y,np.arange(1,300),'gaus1',2)
#print(coef)
print(freqs)
plt.matshow(coef) # doctest: +SKIP
plt.show() # doctest: +SKIP300