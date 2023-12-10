import numpy as np
import matplotlib.pyplot as plt

#carrier signal
fc = 100
t = np.arange(0,.2,1/2000)
carrier_amplitude = np.sin(2*np.pi*fc*t)
plt.subplot(3,1,1)
plt.grid(True)
plt.title("Carrier Siganl")
plt.plot(t, carrier_amplitude);

#modulating signal
modulating_amplitude = (np.sin(2*np.pi*30*t) + np.sin(2*np.pi*45*t))
plt.subplot(3,1,2)
plt.title("Modulating Siganl")
plt.grid(True)
plt.plot(t, modulating_amplitude);

#modulated signal
modulated_time = np.arange(0,.2,1/2000)
modulated_amplitude = np.sin(2*np.pi*fc*t + modulating_amplitude)
plt.subplot(3,1,3)
plt.grid(True)
plt.title("Modulated Siganl")
plt.plot(modulated_time, modulated_amplitude, color='red');

plt.show()

# import numpy as np
# import matplotlib.pyplot as plt

# fig, axis = plt.subplots(nrows=3, ncols=1)
# #carrier signal
# c_f = 16 #carrier frequency
# c_a = 2 #carrier amplitude
# c_p = 0 #carrier phase
# c_time = np.arange(0,1,1/8000)
# c_amplitude = c_a*np.cos(2*np.pi*c_f*c_time + c_p)
# axis[0].grid(True)
# axis[0].set_title("Carrier Siganl")
# axis[0].plot(c_time, c_amplitude);

# #message signal
# m_f = 5 #message frequency
# m_amp = 1 #message ampltude
# m_phase = 0 #message Phase
# m_time = np.arange(0,1,1/8000) 
# thita = 2*np.pi*m_f*m_time + m_phase
# m_amplitude = m_amp*np.cos(2*np.pi*m_f*m_time + m_phase)
# axis[1].set_title("Modulating Siganl")
# axis[1].grid(True)
# axis[1].plot(m_time, m_amplitude);

# #modulated signal
# modulated_freq = 10
# modulated_time = np.arange(0,1,1/8000)
# modulated_amplitude = np.cos(2*np.pi*modulated_freq*modulated_time + m_amplitude)
# axis[2].grid(True)
# axis[2].set_title("Modulated Siganl")
# axis[2].plot(modulated_time, modulated_amplitude, color='red');

# plt.show()