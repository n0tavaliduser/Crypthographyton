# authored by NAVU

class Polyalphabetic(object):
    def __init__(self):
        self.reset()

    def reset(self):
        self.alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ "
        self.plaintext = []
        self.key = []

    def setPlaintext(self, plaintextInput):
        self.plaintext = plaintextInput.split()

    def setKey(self, keyInput):
        if self.plaintext == "":
            print("plaintext belum ada")
            return
        else:
            keyIndex = 0
            for i in range(len(self.plaintext)):
                for y in range(len(self.plaintext[i])):
                    if keyIndex == len(keyInput):
                        keyIndex*=0
                    self.key+=keyInput[keyIndex]
                    keyIndex+=1

    def encode(self):
        ptIndex = []
        for x in range(len(self.plaintext)):
            for y in range(len(self.plaintext[x])):
                ptIndex.append(self.alphabet.index(self.plaintext[x][y]))

        for x in range(len(self.key)):
            ptIndex[x]+=self.alphabet.index(self.key[x])
            if ptIndex[x]>25:
                ptIndex[x]-=26
        
        ciphertext = ""
        for x in range(len(ptIndex)):
            ciphertext+=self.alphabet[ptIndex[x]]
        
        return ciphertext

    def decode(self):
        keyIndex = []
        for x in range(len(self.encode())):
            keyIndex.append((self.alphabet.index(self.encode()[x]))-self.alphabet.index(self.key[x]))
        
        originalPlaintext = ""
        for i in range(len(keyIndex)):
            if keyIndex[i] < 0:
                keyIndex[i]+=26
            originalPlaintext+=self.alphabet[keyIndex[i]]

        return originalPlaintext