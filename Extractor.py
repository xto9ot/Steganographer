print("------------------------------------------------------------------")
print("-----------------Image Steganography Extractor--------------------")
print("------------------------------------------------------------------")
while(True):
    try:
        from cryptosteganography import CryptoSteganography
        from cryptography.fernet import Fernet
        Key=input("Enter the decryption key:")
        file_key=input("Enter your file key:")
        img_name=input("Enter the image path:")
        save_file=input("Enter the name of the output file:")
        x= Fernet(Key)
        crypto_steganography = CryptoSteganography(file_key)
        with open(save_file,'wb') as file:
            secret= crypto_steganography.retrieve(img_name)
            decrypted_secret=x.decrypt(secret)
            file.write(decrypted_secret)
            print(f"Saved as {save_file}")
            break
    except:
        print("Install CryptoSteganography and cryptography Libraries First!")
        break
