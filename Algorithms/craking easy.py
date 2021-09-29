import crypt

def testPass(cryptPass): # Toma el password encriptado
    salt = cryptPass[0:2]
    dictFile = open('dictionary.txt', 'r')
    for word in dictFile.readlines(): # Busca en el diccionario
        word = word.strip('\n')
        cryptWord = crypt.crypt(word, salt)
        if cryptWord == cryptPass: # Si encuntra la palabra la debuelve
            print ("[+] Found Password: " + word + "\n")
            return
    print("[-] Password Not Found. \n")
    return

def main():
    passFile = open('passwords.txt') # Itera sobre todos lo password encriptados
    for line in passFile.readlines():
        if ":" in line:
            user = line.split(":")[0]
            cryptPass = line.split(":")[1].strip(" ")
            print("[*] Craking Password For: ", user)
            testPass(cryptPass)

if __name__ == "__main__":
    main()
