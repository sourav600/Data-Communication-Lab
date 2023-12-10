import numpy as np
import matplotlib.pyplot as plt
def signalPloting(bits):
    x=0
    f = 1 #Amplitude and frequency remain same
    phase1=0
    phase2=np.pi/2 #90 degree = pi/2 radian
    phase3=np.pi # 180 degree = pi redian
    phase4=(3*np.pi)/2 #270 degree =  (3*pi)/2 radian

    for i in range(0,len(bits),2):
        if i+1 >= len(bits):
            break
        time = np.arange(x,x+2, 1/1000)
        if (bits[i]=='0' and bits[i+1]=='0'):
            amp = np.sin(2*3.14*f*time + phase1) #2*pi*f*T
        elif(bits[i]=='0' and bits[i+1]=='1'):
            amp = np.sin(2*3.14*f*time + phase2)
        elif(bits[i]=='1' and bits[i+1]=='0'):
            amp = np.sin(2*3.14*f*time + phase3)
        elif(bits[i]=='1' and bits[i+1]=='1'):
            amp = np.sin(2*3.14*f*time + phase4)
        x = x+2
        plt.plot(time, amp)

while True:
    inp = input("Enter digital data: ")
    if (inp==" "):
        break
    signalPloting(inp)
    plt.grid(True)
    plt.title("Dibit Phase Shift Keying")
    plt.xlabel("Time")
    plt.ylabel("Amplitude")
    plt.plot([0, len(inp)],[0,0], color='black')
    plt.plot([0,0],[-2,2], color='black')
    plt.show()