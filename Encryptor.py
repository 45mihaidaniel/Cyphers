from Cyph import CCD,CCE
import time
print("""Hello!
I can Encrypt or Decrypt your messages,
put your message in the insert.txt file
and choose the operation you need""")
dec=input("What do you need me for? E/D: ")
if dec=="E":
   stream=open("Insert.txt","r")
   ch=""
   for c in stream.read():
      ch+=c
   stream.close()
   E=CCE(ch)
   print("Your file is encrypting...")
   time.sleep(3)
   file=open("new.txt","w")
   file.write(E)
   file.close()
   print("""Done!
         Check 'new.txt' for your encrypted message.""")
   time.sleep(3)
elif dec=="D":
   stream=open("Insert.txt","r")
   ch=""
   for c in stream.read():
      ch+=c
   stream.close()
   E=CCD(ch)
   print("Your file is decrypting...")
   time.sleep(3)
   file=open("new.txt","w")
   file.write(E)
   file.close()
   print("""          Done!
         Check 'new.txt' for your decrypted message.""")
   time.sleep(3)
