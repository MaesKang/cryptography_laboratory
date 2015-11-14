## Autokey Cipher

def AutoKeyCipher(plaintext, key):    
    Matrix = [['0' for x in range(26)] for x in range(26)]
    for i in range(26):
        for j in range(26):
            Matrix[i][j] = chr((j + i) % 26 + ord('A'))
    if(len(key) < len(plaintext)):
        key = key + plaintext

    for i in range(len(plaintext)):
        r = ord(plaintext[i]) - ord('A')
        c = ord(key[i]) - ord('A')
        print Matrix[r][c],

if __name__ == "__main__":
    plaintext = raw_input("Enter the Plaintext: ")
    key = raw_input("Enter the Key: ")

    #Autokey Cipher
    AutoKeyCipher(plaintext, key)
