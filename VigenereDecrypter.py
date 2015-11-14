import operator
from freqAnalysis import *



#Ciphertext = "CHREEVOAHMAERATBIAXXWTNXBEEOPHBSBQMQEQERBWRVXUOAKXAOSXXWEAHBWGJMMQMNKGRFVGXWTRZXWIAKLXFPSKAUTEMNDCMGTSXMXBTUIADNGMGPSRELXNJELXVRVPRTULHDNQWTWDTYGBPHXTFALJHASVBFXNGLLCHRZBWELEKMSJIKNBHWRJGNMGJSGLXFEYPHAGNRBIEQJTAMRVLCRREMNDGLXRRIMGNSNRWCHRQHAEYEVTAQEBBIPEEWEVKAKOEWADREMXMTBHHCHRTKDNVRZCHRCLQOHPWQAIIWXNRMGWOIIFKEE"
Ciphertext = "KCCPKBGUFDPHQTYAVINRRTMVGRKDNBVFDETDGILTXRGUDDKOTFMBPVGEGLTGCKQRACQCWDNAWCRXIZAKFTLEWRPTYCQKYVXCHKFTPONCQQRHJVAJUWETMCMSPKQDYHJVDAHCTRLSVSKCGCZQQDZXGSFRLSWCWSJTBHAFSIASPRJAHKJRJUMVGKMITZHFPDISPZLVLGWTFPLKKEBDPGCERSHCTJRWXBAFSPEZQNRWXCVYCGAONWDDKACKAWBBIKFTIOVKCGGHJVLNHIFFSQESVYCLACNVRWBBIREPBBVFEXOSCDYGZWPFDTKFQIYCWHJVLNHIQIBTKHLTVNPIST"

def ShiftCipher(plaintext, key):
    l = len(plaintext)
    CipherText = ''
    for i in range(l):
        CipherText = CipherText + chr((ord(plaintext[i]) - ord('A') + key) % 26 + ord('A')) 

    return CipherText

def Factors(n):
    l = []
    for i in range(2,n):
        if(n%i == 0):
            l.append(i)
    return l

Substrings = []
for i in range(len(Ciphertext) - 3):
    Substrings.append(Ciphertext[i:i+3])

UniqueSubstrings = list(set(Substrings))

CountTable = []
for i in range(len(UniqueSubstrings)):
    temp1 = Substrings.count(UniqueSubstrings[i])
    if(temp1 >= 2):
        index = Ciphertext.find(UniqueSubstrings[i])
        temp2 = Ciphertext[index+3:]
        CountTable.append([UniqueSubstrings[i], temp1, temp2.find(UniqueSubstrings[i]) + 3])
print "Frequency Table: "
Distances = []
for i in range(len(CountTable)):
    print CountTable[i]
    Distances.append(CountTable[i][2])

FactorsTable = {}
for d in Distances:
    factors = Factors(d)
    for f in factors:
        if(FactorsTable.get(f) == None):
            FactorsTable[f] = 1
        else:
            FactorsTable[f] += 1

FactorsTable = sorted(FactorsTable.items(), key=operator.itemgetter(1))

print FactorsTable

for i in xrange(len(FactorsTable)-1, len(FactorsTable)-2, -1):
    print FactorsTable[i]
    n = FactorsTable[i][0]
    l = []
    PossibleLetters= []
    for j in range(n):
        l.append('')
        PossibleLetters.append('')
    for i in range(len(Ciphertext)):
        l[i%n] += Ciphertext[i]
    for j in range(n):
        print l[j]
        print
        print
    
    for j in range(n):
        temp = []
        for k in range(26):
            message = ShiftCipher(l[j], k) 
            temp.append(englishFreqMatchScore(message))
        print
        print temp
        max(temp)
        for k in range(26):
            if (temp[k] == max(temp)):
                print k
                PossibleLetters[j] += chr( k + ord('A'))
        print PossibleLetters[j]



