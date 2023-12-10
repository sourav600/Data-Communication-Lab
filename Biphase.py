import numpy as np
import matplotlib.pyplot as plt

def getDmanSignal(bits):
    x_cor = []
    y_cor = []
    x=0
    last_y = 1
    for bit in bits:
        if bit=='0':
            x_cor.append(x)
            y_cor.append(-last_y)
            last_y = -last_y
            
        x_cor.append(x)
        y_cor.append(last_y)
        x_cor.append(x+1)
        y_cor.append(last_y)
        x_cor.append(x+1)
        y_cor.append(-last_y)
        x_cor.append(x+2)
        y_cor.append(-last_y)

        last_y = -last_y
        x = x+2
    return [x_cor,y_cor]
def getManchesterSignal(bits):
    x_cor = []
    y_cor = []
    x=0
    for bit in bits:
        if bit=='1':
            x_cor.append(x)
            y_cor.append(-1)
            x_cor.append(x+1)
            y_cor.append(-1)
            x_cor.append(x+1)
            y_cor.append(1)
            x_cor.append(x+2)
            y_cor.append(1)
        else:
            x_cor.append(x)
            y_cor.append(1)
            x_cor.append(x+1)
            y_cor.append(1)
            x_cor.append(x+1)
            y_cor.append(-1)
            x_cor.append(x+2)
            y_cor.append(-1)
        x = x+2
    return [x_cor,y_cor]

while True:
    inp = input('Enter your digital signal :')

    if(inp is ''):
        break
    inp = str(inp)

    fig, axis = plt.subplots(nrows=1, ncols=2)
    plt.tight_layout()

    sig1 = getManchesterSignal(inp)
    sig2 = getDmanSignal(inp)
    plt.xlabel("Time")
    plt.ylabel("Amplitude")
    axis[0][0].set_title("Manchester representation")
    axis[0][1].set_title("Differential Manchester representation")

    x = np.arange(0,len(sig1[0])/2)
    y=[0]*(len(sig1[0])/2)
    axis[0][0].scatter(x,y,marker ="." )

    # Manchester representation
    axis[0][0].grid(True)
    axis[0][1].grid(True)
    axis[0][0].plot([0,len(sig1[0])/2],[0,0],color='black')
    axis[0][1].plot([0,len(sig2[0])/2],[0,0],color='black')
    axis[0][0].plot([0,0],[-2,2],color='black')
    axis[0][1].plot([0,0],[-2,2],color='black')
    axis[0][0].plot(sig1[0],sig1[1],color='red')
    axis[0][1].plot(sig2[0],sig2[1],color='red')
    plt.show()