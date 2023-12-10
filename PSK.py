import numpy as np
import matplotlib.pyplot as plt
def signalPloting(bits):
    x=0
    f = 1 #Amplitude and frequency remain same
    phase1=0
    phase2=np.pi # 180 degree = pi redian
    for bit in bits:
        time = np.arange(x,x+2, 1/1000)
        if (bit=='1'):
            amp = np.sin(2*3.14*f*time + phase1) #2*pi*f*T
        else:
            amp = np.sin(2*3.14*f*time + phase2)
        x = x+2
        plt.plot(time, amp)

while True:
    inp = input("Enter digital data: ")
    if (inp==" "):
        break
    signalPloting(inp)
    plt.grid(True)
    plt.title("Phase Shift Keying")
    plt.xlabel("Time")
    plt.ylabel("Amplitude")
    plt.plot([0, len(inp)*2],[0,0], color='black')
    plt.plot([0,0],[-2,2], color='black')
    plt.show()