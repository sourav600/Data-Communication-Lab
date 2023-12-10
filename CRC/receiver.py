import numpy as np
def xor(a,b):
    result = []
    for i in range(1,len(b)):
        if a[i]==b[i]:
            result.append('0')
        else:
            result.append('1')
    return ''.join(result)
    
def division(dividend, divisor):
    l = len(divisor)
    temp = dividend[0:l]
    while l < len(dividend):
        if temp[0]=='1':
            temp = xor(divisor, temp) + dividend[l]
        else:
            temp = xor('0'*l , temp) + dividend[l]
        l = l+1

    if temp[0]=='1':
        temp = xor(divisor, temp)
    else:
        temp = xor('0'*l , temp)

    return temp

inp = input("Enter recieved to send: ")
divisor = input("Enter the divisor: ")

# data = (''.join(format(ord(ch),'b') for ch in inp))
# print("Binary data: ", data)

append_data = inp + '0'*(len(divisor)-1)
reminder = division(append_data, divisor)

print("Reminder: ",reminder)
flag = 0
for r in reminder:
    if r=='1':
        flag=1
if flag==0:
    print("Data has no error.")
else:
    print("Data contain error.")

