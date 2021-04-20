from monoalphabetic import Monoalphabetic
from polyalphabetic import Polyalphabetic
from playfair import Playfair
import os

def cls():
    os.system('cls' if os.name=='nt' else 'clear')

def main():
    keepRun = True
    while keepRun:
        cls()
        print("=====Encryption=====")
        print("1. Monoalphabetic Cipher")
        print("2. Polyalphabetic Cipher")
        print("3. Playfair Cipher")
        print("0. EXIT")
        choose = str(input("pilihan --> "))
        if choose == "1":
            plaintext = str(input("plaintext\t: "))
            key = str(input("kata kunci\t: "))
            mono.setPlaintext(plaintext)
            mono.setKey(key)
            print("ciphertext\t:",mono.encode())
            print("Original text\t:",mono.decode())
            enter = input("press ENTER to continue ... ")
            mono.reset()
        elif choose == "2":
            plaintext = str(input("plaintext\t: "))
            key = str(input("kata kunci\t: "))
            poly.setPlaintext(plaintext)
            poly.setKey(key)
            print("ciphertext\t:",poly.encode())
            print("Original text\t:",poly.decode())
            enter = input("press ENTER to continue ... ")  
            poly.reset()   
        elif choose == "3":
            plaintext = str(input("plaintext\t: "))
            key = str(input("kata kunci\t: "))
            play.setPlaintext(plaintext)
            play.setKey(key)
            print("kata kunci : ")
            play.printKey()
            print("plaintext\t:",play.printPlaintext())
            print("ciphertext\t:",play.encode())
            enter = input("press ENTER to continue ... ")  
            play.reset()   
        elif choose == "0":
            keepRun = False       
if __name__ == "__main__":
    mono = Monoalphabetic()
    poly = Polyalphabetic()
    play = Playfair()
    main()