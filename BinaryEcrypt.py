#newencryptor
#encrptor
import time
global crypted
target=input("Enter your message for encrption:")
crypted=[]
for ch in target:
    if ch.isalpha()==False:
        continue
    x=bin(ord(ch))
    crypted.append(x.split("0b")[1])

written=""
for elem in crypted:
        written+=elem
print("Your encrypted message is:",written,sep="\n")

decision=input("Would you like to decrypt it?(Y/N):")
if decision in ["y","Y"]:
    decr=""
    for elem in crypted:
        decr+=chr(int(elem,2))
    print("Your decrypted text is:",decr,sep="\n")
elif decision in ["n","N"]:
    print("That's all!","Bye Bye!",sep="\n")
    time.sleep(1)



