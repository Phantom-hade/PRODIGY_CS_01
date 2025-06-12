"""
Title       : Caesar Cipher Program
Author      : Larona B. Kwae
Date        : June 2025
PRODIGY_CS  : 02
Description : A python program that encrypts and decrypts a message using the Caesae Cipher Algorithm
""" 
#prompt user for input
message = input("Enter your message: ")
encryptedmessage = input("Enter message to decrypt: ")
s = int(input("Enter your shift value: "))

#Encryption Code
def encrypt(message,s):
    encrypted = ""    

    #transverse through each character in plain message
    for i in range(len(message)):
        char = message[i]

        #Encrypt uppercase characters in plain message
        if(char.isupper()):
            encrypted += chr((ord(char) + s - 65) % 26 + 65)

        #Encrypt lowercase characters in plain message   
        elif char.islower():
            encrypted += chr((ord(char) + s - 97) % 26 + 97)   

         #leave non letters as is   
        else:
            encrypted += char 
    return encrypted

#Decryption Code
def decrypt(message,s):
    dencrypted = ""

    #transverse through plain message
    for i in range(len(message)):
        char = message[i]

        #Decrypt uppercase characters in plain message
        if(char.isupper()):
            dencrypted += chr((ord(char) - s - 65 ) % 26 + 65) 

         #Decrypt lowercase characters in message
        elif char.islower():  
            dencrypted+= chr((ord(char) - s - 97) % 26 + 97)

          #leave non letters as is   
        else:
            dencrypted += char    
    return dencrypted

print("Plain message: ",message)
print("Shift: ",s)          
print("Cipher-Encrypt: ",encrypt(message,s))
print("Cipher-Decrypt: ",decrypt(encryptedmessage,s))