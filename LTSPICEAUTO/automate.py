import ltspice 
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import numpy as np 
import os  
from PyLTSpice.LTSpice_RawRead import LTSpiceRawRead

l = ltspice.Ltspice('try.raw')
l.parse()


noise = l.get_data('V(onoise)')
gain = l.get_data('gain')

freq = l.get_data('frequency')


fig, ax = plt.subplots(2, constrained_layout=True)
ax[0].semilogy(freq, gain)
ax[1].plot(freq, noise)

ticks = ticker.FuncFormatter(lambda x, pos: '{0:g}'.format(x*10**(-6)))
ax[0].xaxis.set_major_formatter(ticks)
ax[1].xaxis.set_major_formatter(ticks)
#plt.yscale('log',base=10) 

#ax[0].set_title('Gain')
ax[0].set_ylabel('Gain(dB)')
#ax[1].set_title('Noise')
ax[1].set_xlabel('Frequency (MHz)')
ax[1].set_ylabel('Noise (V/$\sqrt{Hz}$)')



plt.legend()
plt.show()

