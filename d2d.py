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

def rzSignal(bits):
    x_cor = []
    y_cor = []
    x=0
    for bit in bits:
        if bit=='1':
            x_cor.append(x)
            y_cor.append(1)
            x_cor.append(x+.5)
            y_cor.append(1)
        else:
            x_cor.append(x)
            y_cor.append(-1)
            x_cor.append(x+.5)
            y_cor.append(-1)
        x_cor.append(x+.5)
        y_cor.append(0)
        x_cor.append(x+1)
        y_cor.append(0)
        x = x+1
    return [x_cor,y_cor]

def nrziSignal(bits):
    x_cor = []
    y_cor = []
    x_cor.append(0)
    y_cor.append(1)
    x=1
    for bit in bits:
        if bit=='1':
            if y_cor[-1]==1:
                x_cor.append(x-1)
                y_cor.append(-1)
                y_cor.append(-1)
            else:
                x_cor.append(x-1)
                y_cor.append(1)
                y_cor.append(1)
        else:
            y_cor.append(y_cor[-1])
        x_cor.append(x)
        x = x+1
    print('NRZ-I coordinates: ')
    print('x is :',x_cor)
    print('Y is :',y_cor)
    return [x_cor,y_cor]    

def nrzlSignal(bits):
    x_co = []
    y_co = []
    x_co.append(0)
    if bits[0]=='1':
        y_co.append(-1)
    else:
        y_co.append(1)
    x = 1
    for bit in bits:
        if bit is '1':
            if y_co[-1]==1:
                x_co.append(x-1)
                y_co.append(-1)
                y_co.append(-1)
            else:
                y_co.append(-1)
        else:
            if y_co[-1] is -1:
                x_co.append(x-1)
                y_co.append(1)
                y_co.append(1)
            else:
                y_co.append(1)
        x_co.append(x)
        x = x+1
    print('x is :',x_co)
    print('Y is :',y_co)
    return [x_co, y_co]

def uniSignal(bits): #Unipolar Function
    x_cor = []
    y_cor = []
    x_cor.append(0)
    y_cor.append(0)
    x=1

    for bit in bits:
        if bit=='1':
            if y_cor[-1] == 1:
                x_cor.append(x)
                y_cor.append(1)
            else:
                x_cor.append(x-1)
                y_cor.append(1)
                x_cor.append(x)
                y_cor.append(1)
        else:
            if y_cor[-1]==0:
                x_cor.append(x)
                y_cor.append(0)
            else:
                x_cor.append(x-1)
                y_cor.append(0)
                x_cor.append(x)
                y_cor.append(0)
        x = x+1
    print('Unipolar coordinates: ')
    print('X: ',x_cor)
    print('Y: ',y_cor)
    return [x_cor,y_cor]


inp = input("Enter digital signal: ")
inp = str(inp)

sig1 = uniSignal(inp)
sig2 = nrzlSignal(inp)
sig3 = nrziSignal(inp)
sig4 = rzSignal(inp)
sig5 = getManchesterSignal(inp)
sig6 = getDifferentialManchesterSignal(inp)

x = np.arange(0,len(inp)+1,1)
y = [0]*(len(inp)+1)

fig, axis = plt.subplots(nrows=3, ncols=2)
plt.tight_layout()

plt.suptitle("Linecoding Techniques")
plt.xlabel("Time");
plt.ylabel("Amplitude")
axis[0,0].grid(True)
axis[0,1].grid(True)
axis[1,0].grid(True)
axis[1,1].grid(True)
axis[2,0].grid(True)
axis[2,1].grid(True)
axis[0,0].set_title("Unipolar represntation")
axis[0,1].set_title("NRZ-L represntation")
axis[1,0].set_title("NRZ-I represntation")
axis[1,1].set_title("RZ represntation")
axis[2,0].set_title("Manchester represntation")
axis[2,1].set_title("Differential Manchester represntation")

#mark each point on x-axis
axis[0,0].scatter(x,y,marker=".")
axis[0,1].scatter(x,y,marker=".")
axis[1,0].scatter(x,y,marker=".")
axis[1][1].scatter(x,y,marker=".")
axis[2][0].scatter(x,y,marker=".")
axis[2][1].scatter(x,y,marker=".")

#Draw x-axis and y-axis
axis[0,0].plot([0,len(inp)+1], [0,0],color='black')
axis[0,0].plot([0,0],[-2,2], color='black')
axis[0,1].plot([0,len(inp)+1], [0,0],color='black')
axis[0,1].plot([0,0],[-2,2], color='black')
axis[1,0].plot([0,len(inp)+1], [0,0],color='black')
axis[1,0].plot([0,0],[-2,2], color='black')
axis[1][1].plot([0,len(inp)+1],[0,0],color='black')
axis[1][1].plot([0,0],[-2,2],color='black')
axis[2][0].plot([0,len(inp)+1],[0,0],color='black')
axis[2][0].plot([0,0],[-2,2],color='black')
axis[2][1].plot([0,len(inp)+1],[0,0],color='black')
axis[2][1].plot([0,0],[-2,2],color='black')

#signal plotting
axis[0,0].plot(sig1[0],sig1[1], color='red') #unipolar signal 
axis[0,1].plot(sig2[0],sig2[1], color='red')#NRZ-L signal
axis[1,0].plot(sig3[0],sig3[1], color='red')#NRZ-I signal
axis[1][1].plot(sig4[0],sig4[1],color='red')#RZ signal
axis[2][0].plot(sig5[0],sig5[1],color='red') #Manchester
axis[2][1].plot(sig6[0],sig6[1],color='red') #Differential Manchester

plt.show()