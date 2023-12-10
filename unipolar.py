import numpy as np
import matplotlib.pyplot as plt

def uniSignal(bits): #Uniporlar function
    print('The input signal is: ',bits)
    x_co = []
    y_co = []
    x_co.append(0)
    y_co.append(0)
    x = 1
    for bit in bits:
        if bit == '1':
            if y_co[-1] == 1:
                y_co.append(1)
            else:
                x_co.append(x-1)
                y_co.append(1)
                y_co.append(1)
        else:
            if y_co[-1] == 0:
                y_co.append(0)
            else:
                x_co.append(x-1)
                y_co.append(0)
                y_co.append(0)
        x_co.append(x)
        x = x+1
    print('x is :',x_co)
    print('Y is :',y_co)
    return [x_co,y_co]

#Ploting
inp = input('Enter your digital signal :')
sig = uniSignal(inp)

x=np.arange(0,len(inp)+2,1)
y=[0]*(len(inp)+2)

#Axis Ploting
plt.grid()
plt.xlabel("Time")
plt.ylabel("Amplitude")
plt.title('Unipolar Representation :'+inp)
plt.scatter(x,y)
#x-axis y-axis
plt.plot([0,len(inp)+2],[0,0],color='black')
plt.plot([0,0],[-2,2],color='black')

#unipolar signal
plt.plot(sig[0],sig[1],color='red')


plt.show()