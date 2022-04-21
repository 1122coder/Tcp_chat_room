import getpass
import  socket
import string


def decrypt(text, shift):
    """ when the shift is known """
    decrypted_text = list(range(len(text)))
    alphabet = string.ascii_lowercase
    first_half = alphabet[:shift]
    second_half = alphabet[shift:]
    shifted_alphabet = second_half + first_half

    for i, letter in enumerate(text.lower()):

        if letter in alphabet:
            index = shifted_alphabet.index(letter)
            original_letter = alphabet[index]
            decrypted_text[i] = original_letter
        else:
            decrypted_text[i] = letter

    return "".join(decrypted_text)


def brute_force_decrypt(text):
    """ when the shift is unknown """
    for n in range(26):
        print(f"Using a shift value of {n}")
        print(decrypt(text, n))
        print("\n***\n")


server_socket=socket.socket();
server_host=socket.gethostname();
ip =socket.gethostbyname(server_host);
sport=8080;

print("This is your ip address: ",ip);
server_host=input("Enter friend's ip address: ");

name=input("Enter your name: ")
server_socket.connect((server_host , sport))
server_socket.send(name.encode())
server_name=server_socket.recv(1024)
server_name=server_name.decode()


server_socket.send(name.encode())

print("",server_name )
while True:
    message= (server_socket.recv(1024)).decode()

    print("Me:",message)
    brute_force_decrypt(message)
    message= input("Me: ")
    server_socket.send(message.encode())


