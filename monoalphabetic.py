# authored by NAVU

class Monoalphabetic(object):
    def __init__(self):
        self.reset()

    def reset(self):
        self.alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        self.plaintext = ""
        self.key = ""
    
    def setKey(self, keyInput):
        for x in range(len(keyInput)):
            if not keyInput[x].split():
                pass
            elif keyInput[x] in self.key:
                pass
            else:
                self.key+=keyInput[x]
            if x == len(keyInput)-1:
                for y in range(len(self.alphabet)):
                    if self.alphabet[y] not in self.key:
                        self.key+=self.alphabet[y]

    def setPlaintext(self, plaintextInput):
        for x in range(len(plaintextInput)):
            if not plaintextInput[x].split():
                pass
            else:
                self.plaintext+=plaintextInput[x]

    def encode(self):
        ciphertext = ""
        for x in range(len(self.plaintext)):
            ciphertext+=self.key[self.alphabet.index(self.plaintext[x])]
        return ciphertext

    def decode(self):
        originalPlaintext = ""
        for i in range(len(self.encode())):
            originalPlaintext+=self.alphabet[self.key.index(self.encode()[i])]
        return originalPlaintext