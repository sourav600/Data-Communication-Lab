import numpy as np

inp = input("Enter received data: ")
l = len(inp)

# generate data with redundant bits (insert 0 for each redundant bit)
pos=0
parity_bits = []
#redundant bit generation
for i in range(1,l+1):
    if(np.log2(i) == int(np.log2(i))):
        print("Calculate redunadant bit ",i)
        idx = i-1
        parity = 0
        while idx<l:
            for j in range(i):
                if idx>=l:
                    break
                if inp[idx]=='1':
                    parity = parity+1
                print("\t",idx+1,"th bit is ", inp[idx])
                idx = idx+1
            for j in range(i):
                if idx >= l:
                    break
                idx = idx+1
        parity_bits.append(parity%2)
        print("The ",i,"th redundant bit is ", parity%2)
print("Parity bits: ",parity_bits)
error_bit = 0
x = 0
for bit in parity_bits:
    error_bit = error_bit + bit*(2**x)
    x = x+1
print("Error bit is: ",error_bit)
