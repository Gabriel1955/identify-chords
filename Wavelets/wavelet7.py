# import pywt
# import numpy as np
# import matplotlib.pyplot as plt

# num_steps = 512
# x = np.arange(num_steps)
# y = np.sin(2*np.pi*x/300)

# delta_t = x[1] - x[0]
# scales = np.arange(1,num_steps+1)
# wavelet_type = 'morl'
# coefs, freqs = pywt.cwt(y, scales, wavelet_type, delta_t)
# plt.matshow(coefs) 
# plt.show()

import pycwt as wavelet
import numpy as np
import matplotlib.pyplot as plt

num_steps = 1000
x = np.arange(num_steps)
y = np.sin(2*np.pi*x/200) + np.sin(2*np.pi*x/20)

delta_t = x[1] - x[0]
scales = np.arange(1,num_steps+1)
freqs = 1/(wavelet.Morlet().flambda() * scales)
wavelet_type = 'morlet'
print(freqs)
coefs, scales, freqs, coi, fft, fftfreqs = wavelet.cwt(y, delta_t, wavelet=wavelet_type, freqs=freqs)
print(freqs)
plt.matshow(abs(coefs)**2)
plt.show()