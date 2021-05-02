
import numpy as np
import matplotlib.pyplot as plt
from ssqueezepy import ssq_cwt, cwt
from ssqueezepy.visuals import plot, imshow

#%%## Configure, compute, plot ###############################################
wavelet = ('morlet', {'mu': 50})
f, N = 2, 100
t = np.linspace(0, 100, N)
x = np.sin(2* np.pi * f * t) 
Wx, scales, *_ = cwt(x, wavelet, fs=N)
#%%# Show, print max row
# print(Wx)
print(len(Wx))
# print(Wx[1])
# print(len(Wx[1]))


# for wx in Wx:
  # print(wx)
  # print("________________")
  # fig, ax = plt.subplots()
  # ax.plot(t, wx)
  # ax.set(xlabel='time (s)', ylabel='Frequency',
  #      title='About as simple as it gets, folks')
  # ax.grid()
  # plt.show()

imshow(Wx, abs=2, yticks=scales, title="f=%d, N=%d" % (f, N), show=1)
# mxidx = np.where(np.abs(Wx) == np.abs(Wx).max())[0][0]
# print("Max row idx:", mxidx, flush=True)

#%%# Plot aroundI max row
# idxs = slice(mxidx - 30, mxidx + 20)
# Wxz = Wx[idxs]
# imshow(Wxz, abs=1, title="abs(CWT), zoomed", show=0)
# plt.axhline(30, color='r')
# plt.show()

#%%## Animate rows ###########################################################
# def row_anim(Wxz, idxs, scales, superposed=False):
#     mx = np.max(np.abs(Wxz))
#     for scale, row in zip(scales[idxs], Wxz):
#         if row.max() == Wxz.max():
#             plt.plot(row.real, color='r')
#         else:
#             plt.plot(row.real, color='tab:blue')
#         plt.ylim(-1.05*mx, 1.05*mx)
#         if not superposed:
#             plt.annotate("scale=%.1f" % scale, weight='bold', fontsize=14,
#                          xy=(.85, .93), xycoords='axes fraction')
#             plt.show()
#         else:
#             plt.xlim(0, len(row) // 4)
#     plt.show()
#%%
# row_anim(Wxz, idxs, scales)
#%%## Superimpose ####
# row_anim(Wxz, idxs, scales, superposed=True)
#%%## Synchrosqueeze
# Tx, _, ssq_freqs, *_ = ssq_cwt(x, wavelet, t=_t(0, 1, N))
#%%
# imshow(Tx, abs=1, title="abs(SSWT)", yticks=ssq_freqs, show=1)

#%%# Damped pendulum example ################################################
# N, w0 = 4096, 25
# t = _t(0, 6, N)
# s = np.exp(-t) * np.cos(w0 * t)

# w = np.linspace(-40, 40, N)
# S = (1 + 1j * w) / ((1 + 1j * w)**2 + w0**2)

#%%# Plot ####
# plot(s, title="s(t)", show=1)
# plot(w, np.abs(S), title="abs(FT(s(t)))", show=1)

#%%# Now SSWT ##
# wavelet = ('morlet', {'mu': 5})
# Tx, *_ = ssq_cwt(s, wavelet, t=t)
#%%# 'cheat' a little; could use boundary wavelets instead (not implemented)
# aTxz = np.abs(Tx)[:, len(t) // 8:]
# imshow(aTxz, abs=1, title="abs(SSWT(s(t)))", show=1)
#%%
# mxidx = np.where(np.abs(aTxz) == np.abs(aTxz).max())[0][0]
# plot(aTxz[mxidx], title="max row of abs(SSWT(s(t)))", show=1)