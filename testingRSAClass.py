from rsa import RSA

rsa1 = RSA()

N, e = rsa1.getKey()

print("Key Generated: (",N,",",e,")")
input_msg = input("Enter a message to encrypt: ")
m = int(input("Enter plaintext key m: "))

encrypted_msg = rsa1.encryptMessage(m, input_msg)

print("Encrypted Message: \n",encrypted_msg.split("$E~N~D$\n")[1],"\n")

decrypted_msg = rsa1.decryptMessage(encrypted_msg)

print("Decrypted Message: \n",decrypted_msg,"\n")