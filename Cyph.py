#This is a module that contains ciphers for text
#Use the functions to encrypt messages

#Ceaser Cipher with one shift
# A -> Z
# B -> A and so on...
def CCE(text):#Encrypter
   cipher=''
   for char in text:
      if not char.isalpha():
         continue
      char=char.upper()
      code=ord(char)-1
      if code<ord('A'):
         code=ord('Z')
      cipher+=chr(code)
   return cipher
#Decrypter
def CCD(text):
   decrypt=''
   for char in text:
      if not char.isalpha():
         continue
      char=char.upper()
      code=ord(char)+1
      if code>ord('Z'):
         code=ord('A')
      decrypt+=chr(code)
   return decrypt


