import numpy as np
import matplotlib.pyplot as plt
def signalPloting(bits):
    x=0
    f=1
    phase=0 #phase and frequency remain same in ASK
    lo_amp=1
    hi_amp=2
    for bit in bits:
        time = np.arange(x,x+2, 1/1000)
        if (bit=='1'):
            amp = hi_amp*np.sin(2*3.14*f*time + phase) #2*pi*f*T
        else:
            amp = lo_amp*np.sin(2*3.14*f*time + phase)
        x = x+2
        plt.plot(time, amp)

while True:
    inp = input("Enter digital data: ")
    if (inp==" "):
        break
    signalPloting(inp)
    plt.grid(True)
    plt.title("Amplitude Shift Keying")
    plt.xlabel("Time")
    plt.ylabel("Amplitude")
    plt.plot([0, len(inp)*2],[0,0], color='black')
    plt.plot([0,0],[-3,3], color='black')
    plt.show()