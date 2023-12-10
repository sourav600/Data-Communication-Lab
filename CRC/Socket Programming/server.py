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

def encodeData(data, divisor):
   append_data = str(data) + "0"*(len(divisor)-1)
   reminder = division(append_data, divisor)    
   return reminder


s = socket.socket()
port = 12345
s.connect(('127.0.0.1', port))
inp = input("Enter data to send: ")
divisor = input("Enter the divisor: ")

# data = (''.join(format(ord(ch),'b') for ch in inp))
# print("Binary data: ", data)

reminder = encodeData(inp,divisor)
print("Reminder: ",reminder)
crc = inp + reminder
print("Send data: ", crc)
s.sendto(crc.encode(),('127.0.0.1', 12345))
print("Recieved feedback: ",s.recv(1024).decode())
s.close()




