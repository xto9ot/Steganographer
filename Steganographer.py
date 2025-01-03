print("-------------------------------------------------------------")
print("-----------------Image Steganography Tool--------------------")
print("-------------------------------------------------------------")
from cryptosteganography import CryptoSteganography
from cryptography.fernet import Fernet
import re

Key=Fernet.generate_key()
decrpyt_key1=re.sub("b\'","",str(Key))
decrpyt_key=re.sub("'","",decrpyt_key1)
print(f"Heres your Decryption key:{decrpyt_key}")
Img_path=input("Enter the image path:")
OutputImg_path=input("Enter the Output Img Path:")
x=Fernet(Key)
file_key=input("Enter your file key:")
crypto_steganography = CryptoSteganography(file_key)
# Save the encrypted file inside the image
with open("msg.txt",'rb') as file:
    msg=file.read()
    encryptedmsg=x.encrypt(msg)
    crypto_steganography.hide(Img_path, OutputImg_path, encryptedmsg)
    print(f"Saved as {OutputImg_path}")