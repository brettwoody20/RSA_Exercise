from rsa import RSA

rsa1 = RSA()

N, e = rsa1.getKey()

print("Key Generated: (",N,",",e,")")
input_msg = input("Enter a message to encrypt: ")
m = int(input("Enter plaintext key m: "))

encrypted_msg = rsa1.encryptMessage(m, input_msg)

print(encrypted_msg)