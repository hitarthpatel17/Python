print("_______CLASSICAL CEASER CIPHER________")
def encrypt(text,key):
 result = ""
 for i in range(len(text)):
    char = text[i] 
    if char.isupper():
        result += chr((ord(char) + key-64) % 26 + 65)
    else:
        result += chr((ord(char) + key - 96) % 26 + 97)
 return result
def decrypt(cipher_text, key):
 plain_text = ""
 for i in range(len(cipher_text)):
    char = cipher_text[i]
    if char.isupper():
        plain_text += chr((ord(char) - key -65) % 26 + 64)
    else:
        plain_text += chr((ord(char) - key - 97) % 26 + 96)
 return plain_text
text = input("Enter Message : ")
key = int(input("Enter Key : "))
print("Plain Text : " + text)
print("Encryption key : " + str(key))
print("\nENCRYPTION\n")
cipher_text = encrypt(text,key)
print("Cipher Text : " + cipher_text ) 
print("\nDECRYPTION\n")
plain_text = decrypt(cipher_text,key)
print("Plain Text After Decryption : " + plain_text)