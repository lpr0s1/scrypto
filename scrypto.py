import random
import os
import time

bleu = "\33[94m"
cl = "\033[42m"
red = "\033[91m"
nocolor = "\033[0m"
gras = "\033[1m"
orange = "\033[38;5;208m"
bgbleu = "\033[44m"

time.sleep(0.1)
print(cl + "                          ")
time.sleep(0.1)
print(" " + bleu + gras + "                [Scrypto]" + nocolor)
time.sleep(0.1)
print(cl + "   "  + orange + bgbleu + "---proxy443---" + nocolor + cl + "         " + nocolor)

print("\n\n")

data = input("Vos données a garder secretes\n" + bleu + "=> " + nocolor)
key = input("Nommez la variable qui stock vos données\n" + bleu + "=> " + nocolor)

time.sleep(0.1)
print("______________")
time.sleep(0.1)
print("\033[92mSucces!\033[0m")


time.sleep(0.1)
print(red + "Votre variable: " + nocolor + key)

code = key

time.sleep(0.6)
print("_______________")

time.sleep(0.8)
print(red)
print("\n\n  [ Vos données sont consultable dans la variable:  ]\n")

k = data

time.sleep(0.6)
print("       =>  " + bleu + key + nocolor)

time.sleep(0.3)
print(nocolor)
print("Vous seul pouvez consulter les données que vous avez enregistrez, seulement en laissant le script ouvert.")

print("\n\n")

time.sleep(3)

os.system("clear")

while True:
    def help():
        print(gras + "\033[41mCENTRE D AIDE" + nocolor)
        print(bleu + "[-]" + red + "Consulter mes données: [Entrez votre variable]")
        print(bleu + "[-]" + red + "Consulter ma variable: [c]")
        print(bleu + "[-]" + red + "Auto-destruction [o]")
        print(bleu + "[-]" + red + "Aide: [help]")
        
    print(bleu)
    help()
    cdata = input("=>" +  nocolor + "")
    
    if(cdata == key):
        os.system("clear")
        print(gras + "\033[41mMES DONNÉES" + nocolor)
        print("\n")
        print(k)
        print("\n\n")
    if(cdata == "help"):
        os.system("clear")
        help()
    if(cdata == "c"):
        os.system("clear")
        print(gras + "\033[41mMA VARIABLE" + nocolor)
        print("\n")
        print(key)
        print("\n\n")
    if(cdata == "f"):
        os.system("clear")
        os.system("clear")
        os.system("clear")
        os.system("clear")
        os.system("clear")
        os.system("clear")
        os.system("clear")
        os.system("clear")
        help()
    if(cdata == "o"):
        conf = input("Etes vous sur de vouloir auto-detruire vos données ? [y/n]\n" + bleu + "=> " + nocolor)
        if(conf == "y"):
            os.system("clear")
            exit()
        if(conf == "n"):
            os.system("clear")
            help()
