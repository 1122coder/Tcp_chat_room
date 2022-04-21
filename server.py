#importing important libraries
from uuid import getnode as get_mac
#from getmac
import socket
import getpass
import platform

class Ciphering_Algo:
    def ciphering( p_text):
        M_name = "kashif"
        sum = 0
        total = 0
        for v in M_name:
            # print(v)
            sum = sum + ord(v)
            total = total + 1

        # print("Sum of Alphabets number is: ",sum,"Total Number of words are: ", total)
        avg = sum / total
        # print(int(avg))
        shift_key = int(avg % 26)

        # print("Shift Key is:", shift_key)
        Alpa_Array = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
                      'u', 'v', 'w', 'x', 'y', 'z']

        plain_text = p_text
        arr2 = []
        for v in plain_text:
            arr2.append(v)

        # print(arr2)
        arr3 = []
        for a in arr2:
            j = 0
            for b in Alpa_Array:
                if a == b:
                    arr3.append(j)

                j += 1

        # print(arr3)

        # Here every value will be added with shift key and mod of each value is taken. and arr3 will be modified.
        i = 0
        for v in arr3:
            newV = v + shift_key
            newV = newV % 26
            arr3[i] = newV
            i += 1

        # print(arr3)

        i = 0
        for v in arr3:
            arr3[i] = Alpa_Array[v]
            i += 1

        # print('Now the cipher text is:', arr3)
        cipher_text = "".join(arr3)
        # print("Cipher text is : ",cipher_text)
        return cipher_text




#connecting the sockets and recieving the hostname
new_socket =socket.socket()
host_name = socket.gethostname()
s_ip = socket.gethostbyname(host_name)
port = 8080

new_socket.bind((host_name, port))
print("Binding Successfully.")
print("This is your ip: ", s_ip)


name = platform.node()


new_socket.listen(1)
mac=get_mac()
mac = ":".join(['{:02x}'.format((mac>>ele)&0xff)for  ele in range(0,8*6,8)][::-1])
conn, add=new_socket.accept()
conn.send(f"{name} \n {mac}".encode())
print("Received Connection from: ",add[0])
print("Established Connection. Connected from : ",add[0])

client= (conn.recv(1024)).decode()
print(client + " has connected....")


while True:
    message= input("Me: ")
    cipher_text=Ciphering_Algo.ciphering(message);
    conn.send(cipher_text.encode())
    message= conn.recv(1024).decode()
    print(client, ": ", message)



