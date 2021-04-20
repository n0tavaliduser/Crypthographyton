class Playfair(object):
    def __init__(self):
        self.reset()

    def reset(self):
        self.alphabet = "ABCDEFGHIKLMNOPQRSTUVWXYZ"
        self.key = [["" for i in range(5)] for j in range(5)]
        self.plaintext = ""

    def setKey(self, key):
        katakunci = ""
        for x in range(len(key)):
            if not key[x].split():
                pass
            elif key[x] in katakunci:
                pass
            else:
                katakunci+=key[x]
            if x == len(key)-1:
                for y in range(len(self.alphabet)):
                    if self.alphabet[y] not in katakunci:
                        katakunci+=self.alphabet[y]
        
        i = 0
        for x in range(len(self.key)):
            for y in range(len(self.key[x])):
                self.key[x][y]+=katakunci[i]
                i+=1
            if x == len(self.key)-1:
                j = 0
                for z in range(5):
                    self.key[z].append(katakunci[j])
                    j += 5
                self.key.append(["" for a in range(5)])
                for b in range(len(self.key[5])):
                    self.key[5][b]+=self.key[0][b]
        
        return(self.key)
            
    def printKey(self):
        for x in range(len(self.key)):
            for y in range(len(self.key[x])):
                print(self.key[x][y], end=" ")
            print("")

    def printPlaintext(self):
        plaintext = ""
        for x in range(len(self.plaintextForm())):
            for y in range(len(self.plaintextForm()[x])):
                plaintext+=self.plaintextForm()[x][y]
            plaintext+=" "
        return plaintext
    
    def setPlaintext(self, pt):
        for x in range(len(pt)):
            if not pt[x].split():
                pass
            elif pt[x] == "J":
                self.plaintext+="I"
            elif len(self.plaintext)%2!=0:
                if pt[x-1] == pt[x]:
                    self.plaintext+="Z"
                    self.plaintext+=pt[x]
                else:
                    self.plaintext+=pt[x]
            else:
                self.plaintext+=pt[x]
        if len(self.plaintext)%2!=0:
            self.plaintext+="Z"

    def plaintextForm(self):
        kata = [["" for x in range(2)] for j in range(len(self.plaintext)//2)]
        i = 0
        for x in range(len(kata)):
            for y in range(len(kata[x])):
                kata[x][y]+=self.plaintext[i]
                i += 1
        return kata
        
    def encode(self):
        ptIndexX = [[0 for x in range(2)] for y in range(len(self.plaintext)//2)]
        ptIndexY = [[0 for x in range(2)] for y in range(len(self.plaintext)//2)]
        for v in range(len(self.plaintextForm())):
            for w in range(len(self.plaintextForm()[v])):
                for x in range(len(self.key)):
                    for y in range(len(self.key[x])):
                        if self.plaintextForm()[v][w] == self.key[x][y]:
                            break
                    if self.plaintextForm()[v][w] == self.key[x][y]:
                        ptIndexX[v][w]=x
                        ptIndexY[v][w]=y
        
        for x in range(len(ptIndexY)):
            for y in range(len(ptIndexY[x])):
                if ptIndexY[x][y] > 5:
                    ptIndexY[x][y] -= 6
                if ptIndexX[x][y] > 4:
                    ptIndexX[x][y] -= 5

        slideSideways = []
        for x in range(len(ptIndexX)):
            if ptIndexX[x][0] == ptIndexX[x][1]:
                slideSideways.append(x)
        
        swipeUp = []
        for x in range(len(ptIndexY)):
            if ptIndexY[x][0] == ptIndexY[x][1]:
                swipeUp.append(x)

        ciphertext = ""
        for x in range(len(ptIndexY)):
            if x in slideSideways:
                a = ptIndexY[x][1]+1
                b = ptIndexY[x][0]+1
                if a > 5:
                    a -= 6
                elif b > 5:
                    b -= 6
                ciphertext+=self.key[ptIndexX[x][1]][b]
                ciphertext+=self.key[ptIndexX[x][0]][a]
                ciphertext+=" "
            elif x in swipeUp:
                a = ptIndexX[x][1]+1
                b = ptIndexX[x][0]+1
                if a > 5:
                    a -= 6
                elif b > 5:
                    b -= 6
                ciphertext+=self.key[b][ptIndexY[x][0]]
                ciphertext+=self.key[a][ptIndexY[x][1]]
                ciphertext+=" "
            else:
                ciphertext+=self.key[ptIndexX[x][0]][ptIndexY[x][1]]
                ciphertext+=self.key[ptIndexX[x][1]][ptIndexY[x][0]]
                ciphertext+=" "

        return(ciphertext)
            

# P = Playfair()
# P.setKey("TEKNIK INFORMATIKA UDINUS")
# P.printKey()
# P.setPlaintex("TUEVANO TITONDEA")
# P.printPlaintext()
# print("\n")
# print(P.encrypt())