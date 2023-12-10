import numpy as np
import matplotlib.pyplot as plt

fig, axis = plt.subplots(nrows=3, ncols=1)
#carrier signal
carrier_f = 8
carrier_amp = 5
carrier_phase = 0
time = np.arange(0,5,1/100)
carrier_amplitude = carrier_amp*np.sin(2*np.pi*carrier_f*time + carrier_phase)
axis[0].grid(True)
axis[0].set_title("Carrier Siganl")
axis[0].plot(time, carrier_amplitude);

#modulating signal
modulating_f = .5
modulating_amp = 1
modulating_phase = np.pi/2
thita = 2*np.pi*modulating_f*time + modulating_phase
modulating_amplitude = modulating_amp*(np.sin(thita)**3 - np.cos(thita)**2 + np.cos(thita))
axis[1].set_title("Modulating Siganl")
axis[1].grid(True)
axis[1].plot(time, modulating_amplitude);

#modulated signal
modulated_amplitude = (carrier_amp+modulating_amplitude)*np.sin(2*np.pi*carrier_f*time + carrier_phase)
axis[2].grid(True)
axis[2].set_title("Modulated Siganl")
axis[2].plot(time, modulated_amplitude, color='red');

plt.show()