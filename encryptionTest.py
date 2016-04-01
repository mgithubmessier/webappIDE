#import sys
#sys.path.insert(0, '/Users/messier_matthew/Desktop/Classes/ACM/WebIDE/Webapp IDE env/pycrypto-2.6.1/lib/')
#from Crypto.Cipher import AES
import AES

def encrypt(toEncrypt,key):
    print('webappIDE.py:encrypt():toEncrypt: '+toEncrypt)
    encrypter = AES.new(key,AES.MODE_CBC,1)
    encryption = encrypter.encrypt(toEncrypt)
    print('weappIDE.py:encrypt():encryption: '+encryption)
    return encryption
    
def decrypt(toDecrypt,key):
    print('webappIDE.py:decrypt():toDecrypt: ' +toDecrypt)
    decrypter = AES.new(key,AES.MODE_CBC,1)
    decryption = decrypter.decrypt(toDecrypt)
    print('webappIDE.py:decrypt():decryption: ' +decryption)
    return decryption

encryption = encrypt("my encryption","my key")
decrypt(encryption,"my key")