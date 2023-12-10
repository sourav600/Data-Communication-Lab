import numpy as np
import matplotlib.pyplot as plt
def signalPloting(bits):
    x=0
    lo_f=1
    hi_f = 2
    phase=0 #Amplitude and phase remain same
    for bit in bits:
        time = np.arange(x,x+2, 1/1000)
        if (bit=='1'):
            amp = np.sin(2*3.14*hi_f*time + phase) #2*pi*f*T
        else:
            amp = np.sin(2*3.14*lo_f*time + phase)
        x = x+2
        plt.plot(time, amp)

while True:
    inp = input("Enter digital data: ")
    if (inp==" "):
        break
    signalPloting(inp)
    plt.grid(True)
    plt.title("Frequency Shift Keying")
    plt.xlabel("Time")
    plt.ylabel("Amplitude")
    plt.plot([0, len(inp)*2],[0,0], color='black')
    plt.plot([0,0],[-2,2], color='black')
    plt.show()