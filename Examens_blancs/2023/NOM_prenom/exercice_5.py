import numpy as np
import matplotlib.pyplot as plt

from scipy import fft

from scipy.io.wavfile import read
bitrates, data = read("Ketsa_flam_out.wav") # Votre fichier audio doit être dans le même répertoire

song_mono = data[:,0] # On extrait la bande gauche de la sortie stéréo pour en faire un son mono

# Question 1
extract = song_mono[0:20*bitrates]

# Question 2
trans_fourr = fft.fft(extract)
frequencies_array = fft.fftfreq(trans_fourr.size,d=1/bitrates)

# Question 3
fig, ax = plt.subplots(nrows=2,figsize=(16,9))
ax[0].plot(extract)
ax[0].set_xlabel("bits")
mask_1 = frequencies_array >=0
ax[1].plot(frequencies_array[mask_1],np.abs(trans_fourr[mask_1])/np.abs(trans_fourr[mask_1]).max())
ax[1].set_xlim(0,1750)
ax[1].set_ylim(0,0.03)
ax[1].set_xlabel("fréquences (Hz)")
plt.show()

# Question 4
filtered_fft_signal = trans_fourr.copy()
filtered_fft_signal[np.abs(frequencies_array) < 75] = 0
sig_filtred = fft.ifft(filtered_fft_signal)
sig_filtred=np.real(sig_filtred)
plt.figure()
plt.plot(sig_filtred)
plt.show()

# Question 5
from scipy.io.wavfile import write
write("filtered_song_test.wav",bitrates,sig_filtred.astype(np.uint8))


# Question 6
"""
L'aspect étrange de la musique vient du fait que l'on a coupé une partie du signale associé a chaque instrument. Un timbre étant une succession d'harmonique pour chaque note.
"""
