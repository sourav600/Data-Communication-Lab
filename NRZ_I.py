import numpy as np
import matplotlib.pyplot as plt

def getSignal(bits):
    x_co = []
    y_co = []
    x_co.append(0)
    if bits[0]=='1':
        y_co.append(-1)
    else:
        y_co.append(1)
    x = 0
    y=1
    for bit in bits:
        if bit=='1':
            y = -y
            x_co.append(x)
            y_co.append(y)
            x_co.append(x+1)
            y_co.append(y)
        else:
            x_co.append(x+1)
            y_co.append(y)
        x = x+1
    return [x_co,y_co]

# def getSignal(bits):
#     x_cor = []
#     y_cor = []
#     x_cor.append(0)
#     y_cor.append(1)
#     x=1
#     for bit in bits:
#         if bit=='1':
#             if y_cor[-1]==1:
#                 x_cor.append(x-1)
#                 y_cor.append(-1)
#                 y_cor.append(-1)
#             else:
#                 x_cor.append(x-1)
#                 y_cor.append(1)
#                 y_cor.append(1)
#         else:
#             y_cor.append(y_cor[-1])
#         x_cor.append(x)
#         x = x+1
#     print('NRZ-I coordinates: ')
#     print('x is :',x_cor)
#     print('Y is :',y_cor)
#     return [x_cor,y_cor]    

while True:
    inp = input('Enter your digital signal :')
    if inp==" ":
        break
    x = np.arange(0,len(inp)+1)
    y=[0]*(len(inp)+1)
    
    sig = getSignal(inp)
    plt.xlabel("Time")
    plt.ylabel("Amplitude")
    plt.title("NRZ-I representation of \'"+inp+"\'")

    plt.scatter(x,y,marker ="." )
    plt.plot([0,len(inp)+1],[0,0],color='black')
    plt.plot([0,0],[-2,2],color='black')

    # For NRZ-I representation
    plt.grid(True)
    plt.plot(sig[0],sig[1],color='red')
    plt.show()
