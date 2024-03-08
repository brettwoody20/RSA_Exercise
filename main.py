from mod import Mod
from math import gcd
import random


'''
x=5
p=23

y = pow(x, -1, p)
print(y)
'''

primes = [23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 
67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113,
127, 131, 137, 139, 149, 151, 157, 163, 167, 173,
179, 181, 191, 193, 197, 199, 211, 223, 227, 229,
233, 239, 241, 251, 257, 263, 269, 271, 277, 281,
283, 293, 307, 311, 313, 317, 331, 337, 347, 349,
353, 359, 367, 373, 379, 383, 389, 397, 401, 409,
419, 421, 431, 433, 439, 443, 449, 457, 461, 463,
467, 479, 487, 491, 499, 503, 509, 521, 523, 541, 
547, 557, 563, 569, 571, 577, 587, 593, 599]


#CREATE

#generate p, q, N, e
e = 601 

p = primes[random.randint(0, len(primes)-1)]
q = primes[random.randint(0, len(primes)-1)]
totient = (p-1)*(q-1)

while p == q or gcd(e,totient) != 1:
    p = primes[random.randint(0, len(primes)-1)]
    q = primes[random.randint(0, len(primes)-1)]
    totient = (p-1)*(q-1)
    
N = p * q

#ENCRYPT

input_msg = input("Enter a message to encrypt: ")
m_e = int(input("Enter plaintext key m: "))
c_e = Mod(m_e**e, N)


cipher_encrypt = {}
used = []

a = m_e % 19
b = m_e % 41
#for each char
for i in range(32, 127):
    cipher_char = Mod((i*a+b),95)
    check = 0
    while int(cipher_char) in used:
       #print(int(cipher_char), ": Collision")
       cipher_char += 1
       check += 1
       if check > 200:
           print("Timed out: ", int(cipher_char), " in \n", sorted(used))
           sys.exit()
    cipher_encrypt.update({chr(i): chr(int(cipher_char)+32)})
    used.append(int(cipher_char))
    
#uncomment to print out encryption cipher
'''
cipher_key = ""
for key, value in cipher_encrypt.items():
    cipher_key = cipher_key + key + "->" + value + " | "  
print(cipher_key)
'''


encrypted_msg = str(int(c_e)) + "~~\n\n"


for char_ in input_msg:
    encrypted_msg = encrypted_msg + cipher_encrypt.get(char_)
    
print("\nEncrypted Message: \n",encrypted_msg.split("~~\n\n")[1])


#DECRYPT

#retrieve c from msg
c_d = int(encrypted_msg.split("~~\n\n")[0])

#compute m
d_d = pow(e, -1, totient)
m_d = int(Mod(c_d**d_d, N))


#create decryption cipher based on m using a hash function
decipher = {}
used_d = []

a_decrypt = m_d % 19
b_decrypt = m_d % 41
for i in range(32, 127):
    cipher_char2 = Mod((i * a_decrypt + b_decrypt),95)
    check = 0
    while int(cipher_char2) in used_d:
       #print(int(cipher_char), ": Collision")
       cipher_char2 += 1
       check += 1
       if check > 200:
           print("Timed out: ", int(cipher_char2), " in \n", sorted(used_d))
           sys.exit()
    decipher.update({chr(int(cipher_char2)+32): chr(i)})
    used_d.append(int(cipher_char2))
    
decrypted_msg = ""

for character in encrypted_msg.split("~~\n\n")[1]:
    decrypted_msg += decipher.get(character)
    
print("\nDecrypted Message: \n", decrypted_msg)






