import numpy as np
import socket
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

def decodeData(data, divisor):
    l_div = len(divisor)
    append_data = str(data.decode()) + '0'*(l_div-1)
    reminder = division(append_data, divisor)
    return reminder

s = socket.socket()
print("Socket creatred succesfullly!")
port = 12345
s.bind(('',port))
s.listen(5)
print("Socket is listening: ")

while True:
    c, add = s.accept()
    data = c.recv(1024)
    print("Recieved data: ", data.decode())
    if not data:
        break
    
    divisor = "1101"
    reminder = decodeData(data, divisor)
    print("Reminder: ",reminder)

    temp = "0"*(len(divisor)-1)
    if reminder==temp:
        c.sendto(("Data "+data.decode() + 
                  " Have no error").encode(), ('127.0.0.1', 12345))
    else:
        c.sendto(("Error found in data!").encode(),('127.0.0.1',12345))
s.close()