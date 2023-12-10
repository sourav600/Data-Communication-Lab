import numpy as np
import matplotlib.pyplot as plt
def ASKploting(bits):
    x=0
    f=1
    phase=0 #phase and frequency remain same in ASK
    lo_amp=1
    hi_amp=2

    x_co=[]
    y_co=[]
    for bit in bits:
        time = np.arange(x,x+2, 1/1000)
        if (bit=='1'):
            amp = hi_amp*np.sin(2*3.14*f*time + phase) #2*pi*f*T
        else:
            amp = lo_amp*np.sin(2*3.14*f*time + phase)
        x = x+2
        x_co = np.append(x_co,time)
        y_co = np.append(y_co,amp)
    return [x_co, y_co]

def FSKploting(bits):
    x=0
    lo_f=1
    hi_f = 2
    phase=0 #Amplitude and phase remain same

    x_co=[]
    y_co=[]
    for bit in bits:
        time = np.arange(x,x+2, 1/1000)
        if (bit=='1'):
            amp = np.sin(2*3.14*hi_f*time + phase) #2*pi*f*T
        else:
            amp = np.sin(2*3.14*lo_f*time + phase)
        x = x+2
        x_co = np.append(x_co,time)
        y_co = np.append(y_co,amp)
    return [x_co, y_co]
    
def PSKploting(bits):
    x=0
    f = 1 #Amplitude and frequency remain same
    phase1=0
    phase2=np.pi # 180 degree = pi redian

    x_co=[]
    y_co=[]
    for bit in bits:
        time = np.arange(x,x+2, 1/1000)
        if (bit=='1'):
            amp = np.sin(2*3.14*f*time + phase1) #2*pi*f*T
        else:
            amp = np.sin(2*3.14*f*time + phase2)
        x = x+2
        x_co = np.append(x_co,time)
        y_co = np.append(y_co,amp)
    return [x_co, y_co]

def DPSKPloting(bits):
    x=0
    f = 1 #Amplitude and frequency remain same
    phase1=0
    phase2=np.pi/2 #90 degree = pi/2 radian
    phase3=np.pi # 180 degree = pi redian
    phase4=(3*np.pi)/2 #270 degree =  (3*pi)/2 radian

    x_co=[]
    y_co=[]
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
        x_co = np.append(x_co,time)
        y_co = np.append(y_co,amp)
    return [x_co, y_co]

#Main function      
inp = input("Enter digital data: ")
    
ask=ASKploting(inp)
fsk=FSKploting(inp)
psk=PSKploting(inp)
dpsk=DPSKPloting(inp)

fig, axis = plt.subplots(nrows=2, ncols=2)
fig.tight_layout()
plt.xlabel("Time")
plt.ylabel("Amplitude")
plt.suptitle("Encoding of Digital data")

axis[0,0].grid(True)
axis[0,1].grid(True)
axis[1,0].grid(True)
axis[1,1].grid(True)
axis[0,0].set_title("Amplitude Shift Keying")
axis[0,1].set_title("Frequency Shift Keying")
axis[1,0].set_title("Phase Shift Keying")
axis[1,1].set_title("Dibit Phase Shift Keying")


#draw X axis and Y axis
axis[0,0].plot([0, len(inp)*2],[0,0], color='black')
axis[0,0].plot([0,0],[-3,3], color='black')
axis[0,1].plot([0, len(inp)*2],[0,0], color='black')
axis[0,1].plot([0,0],[-2,2], color='black')
axis[1,0].plot([0, len(inp)*2],[0,0], color='black')
axis[1,0].plot([0,0],[-2,2], color='black')
axis[1,1].plot([0, len(inp)],[0,0], color='black')
axis[1,1].plot([0,0],[-2,2], color='black')

axis[0,0].plot(ask[0],ask[1], color='green')
axis[0,1].plot(fsk[0],fsk[1],color='red')
axis[1,0].plot(psk[0],psk[1], color='green')
axis[1,1].plot(dpsk[0],dpsk[1], color='red')

plt.show()