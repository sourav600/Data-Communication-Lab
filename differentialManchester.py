import numpy as np
import matplotlib.pyplot as plt

def getDifferentialManchesterSignal(bits):
    x_cor = []
    y_cor = []
    x=0
    last_y = 1
    for bit in bits:
        if bit=='0':
            x_cor.append(x)
            y_cor.append(last_y)
            x_cor.append(x)
            y_cor.append(-last_y)
            last_y = -last_y
            
        x_cor.append(x)
        y_cor.append(last_y)
        x_cor.append(x+.5)
        y_cor.append(last_y)
        x_cor.append(x+.5)
        y_cor.append(-last_y)
        x_cor.append(x+1)
        y_cor.append(-last_y)

        last_y = -last_y
        x = x+1
    return [x_cor,y_cor]

while True:
    inp = input('Enter your digital signal :')
    if(inp==" "):
        break

    sig = getDifferentialManchesterSignal(inp)
    plt.xlabel("Time")
    plt.ylabel("Amplitude")
    plt.title("Differential Manchester representation of \'"+inp+"\'")

    print('X: ',sig[0])
    print('Y: ',sig[1])
    x = np.arange(0,len(inp))
    y=[0]*len(inp)
    plt.scatter(x,y,marker ="." )

    #Differential Manchester representation
    plt.grid(True)
    plt.plot([0,len(inp)+1],[0,0],color='black')
    plt.plot([0,0],[-2,2],color='black')
    plt.plot(sig[0],sig[1],color='red')
    plt.show()