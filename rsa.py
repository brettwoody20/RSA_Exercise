#Could implement RSA class here

from mod import Mod
from math import gcd
import random

class RSA:

    #static list of primes
    __primes = [23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 
        67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113,
        127, 131, 137, 139, 149, 151, 157, 163, 167, 173,
        179, 181, 191, 193, 197, 199, 211, 223, 227, 229,
        233, 239, 241, 251, 257, 263, 269, 271, 277, 281,
        283, 293, 307, 311, 313, 317, 331, 337, 347, 349,
        353, 359, 367, 373, 379, 383, 389, 397, 401, 409,
        419, 421, 431, 433, 439, 443, 449, 457, 461, 463,
        467, 479, 487, 491, 499, 503, 509, 521, 523, 541, 
        547, 557, 563, 569, 571, 577, 587, 593, 599]
    #e is considered static
    __e = 65537
    
    #constructor generates p, q, N (private variables)
    def __init__(self):
        self.__p = RSA.__primes[random.randint(0, len(RSA.__primes)-1)]
        self.__q = RSA.__primes[random.randint(0, len(RSA.__primes)-1)]
        totient = (self.__p-1)*(self.__q-1)
        
        while self.__p == self.__q or gcd(RSA.__e,totient) != 1:
            self.__p = RSA.__primes[random.randint(0, len(RSA.__primes)-1)]
            self.__q = RSA.__primes[random.randint(0, len(RSA.__primes)-1)]
            totient = (self.__p-1)*(self.__q-1)
            
        self.__N = self.__p * self.__q
    
    #function to get public key N, e
    def getKey(self):
        return self.__N, RSA.__e
    
    #function to encrypt a message using RSA (int m, string plaintext) -> (int c, string encrypted)
    def encryptMessage(self, m, plaintext):
        c = Mod(m**RSA.__e, self.__N)

        cipher_encrypt = {}
        used = []

        a = m % 19
        b = m % 41
        #for each char
        for i in range(32, 127):
            cipher_char = Mod((i*a+b),95)
            while int(cipher_char) in used:
                cipher_char += 1
            cipher_encrypt.update({chr(i): chr(int(cipher_char)+32)})
            used.append(int(cipher_char))
            
        encrypted_msg = str(int(c)) + "$E~N~D$\n"
        for char_ in plaintext:
            encrypted_msg = encrypted_msg + cipher_encrypt.get(char_)
            
        return encrypted_msg
    
    
    #function to decrypt a message using RSA (int c, string encrypted) -> (string plaintext)
    def decryptMessage(self, encrypted):
        #retrieve c from msg
        c = int(encrypted.split("$E~N~D$\n")[0])

        #compute m
        d = pow(RSA.__e, -1, (self.__p-1)*(self.__q-1))
        m = int(Mod(c**d, self.__N))


        #create decryption cipher based on m using a hash function
        decipher = {}
        used = []

        a_decrypt = m % 19
        b_decrypt = m % 41
        for i in range(32, 127):
            cipher_char2 = Mod((i * a_decrypt + b_decrypt),95)
            while int(cipher_char2) in used:
                #print(int(cipher_char), ": Collision")
                cipher_char2 += 1
            decipher.update({chr(int(cipher_char2)+32): chr(i)})
            used.append(int(cipher_char2))
            
        decrypted = ""

        for character in encrypted.split("$E~N~D$\n")[1]:
            decrypted += decipher.get(character)
            
        return decrypted
    
#NOTE: if RSA would be a class stored on a server, then they would not store the p, q values- those would be stored on the client's side 