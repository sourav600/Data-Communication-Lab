import numpy as np
import matplotlib.pyplot as plt

def getManchesterSignal(bits):
    x_cor = []
    y_cor = []
    x=0
    for bit in bits:
        if bit=='1':
            x_cor.append(x)
            y_cor.append(-1)
            x_cor.append(x+.5)
            y_cor.append(-1)
            x_cor.append(x+.5)
            y_cor.append(1)
            x_cor.append(x+1)
            y_cor.append(1)
        else:
            x_cor.append(x)
            y_cor.append(1)
            x_cor.append(x+.5)
            y_cor.append(1)
            x_cor.append(x+.5)
            y_cor.append(-1)
            x_cor.append(x+1)
            y_cor.append(-1)
        x = x+1
    return [x_cor,y_cor]

while True:
    inp = input('Enter your digital signal :')
    if(inp==" "):
        break

    sig = getManchesterSignal(inp)
    plt.xlabel("Time")
    plt.ylabel("Amplitude")
    plt.title("Manchester representation of \'"+inp+"\'")

    print('X: ',sig[0])
    print('Y: ',sig[1])
    
    x = np.arange(0,len(inp))
    y=[0]*len(inp)
    plt.scatter(x,y,marker ="." )

    # Manchester representation
    plt.grid(True)
    plt.plot([0,len(inp)+1],[0,0],color='black')
    plt.plot([0,0],[-2,2],color='black')
    plt.plot(sig[0],sig[1],color='red')
    plt.show()