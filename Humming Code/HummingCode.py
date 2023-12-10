import numpy as np

inp = input("Enter data bits: ")
d = len(inp)
r = int(np.log2(d))
while(2**r < d+r+1):
    r = r+1
l = d+r
print("Data lenght: ",d," Redundant length: ",r);

# generate data with redundant bits (insert 0 for each redundant bit)
pos=0
humming_code = []
for i in range(1,l+1):
    if(np.log2(i) == int(np.log2(i))): #it refers to the redundent bit position
        humming_code.append(0)
    else:
        humming_code.append(ord(inp[pos])-48) #it add the data bit
        pos = pos+1
print("Humming code with all redundant bit '0' ",humming_code)

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
                if humming_code[idx]==1:
                    parity = parity+1
                print("\t",idx+1,"th bit is ", humming_code[idx])
                idx = idx+1
            for j in range(i):
                if idx >= l:
                    break
                idx = idx+1
        humming_code[i-1] = parity%2
        print("The ",i,"th redundant bit is ", parity%2)
print("\nHumming Code is: ",humming_code)