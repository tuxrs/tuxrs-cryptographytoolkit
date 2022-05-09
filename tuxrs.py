
import time
import os 
import pyfiglet
from rich.console import Console
console = Console()
import hashlib

def hash_decryptor():

    flag = 0
    counter = 0

    pass_hash = input("Enter md5 hash: ")

    wordlist = input("filename: ")
    try:
        pass_file = open(wordlist, "r")
    except:
        print("No file found")
        quit()

    for word in pass_file:

        enc_wrd = word.encode('utf-8')
        digest = hashlib.md5(enc_wrd.strip()).hexdigest()
        counter += 1

        if digest == pass_hash:
            print("Password has been found!")
            print("The decrypted password for " + pass_hash + " is:   " + word)
            print("We analyzed " + str(counter) + " passwords from your file.")
            flag = 1
            break

    if flag == 0:
        print("The password is not in your file/list.")



def pw_generatorr():   
   
    import random
    import string

    print('hello, Welcome to Password generator!')

    length = int(input('\nEnter the length of password: '))                      

    lower = string.ascii_lowercase
    upper = string.ascii_uppercase
    num = string.digits
    symbols = string.punctuation

    all = lower + upper + num + symbols

    temp = random.sample(all,length)

    password = "".join(temp)

    print(password)

def sha256():
    string_to_hash = input("ENTER THE STRING TO ENCRYPT: ")
    hash_object = hashlib.sha256(str(string_to_hash).encode('utf-8'))
    print('Hash : ', hash_object.hexdigest())

def sha512():
    string_to_hash = input("ENTER THE STRING TO DECRYPT: ")
    hash_object = hashlib.sha512(str(string_to_hash).encode('utf-8'))
    print('Hash : ', hash_object.hexdigest())

def sha1():
    string_to_hash = input("ENTER THE STRING TO DECRYPT: ")
    hash_object = hashlib.sha1(str(string_to_hash).encode('utf-8'))
    print('Hash : ', hash_object.hexdigest())






def rot_13():

	import sys
	print("the rot 13 decoder")

	try: 
		indice = 26 - int(sys.argv[1])
	except:
		indice = 13 
		
	alpha = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
	while True:
		print("insert the phrase to encrypt or decrypt")
		stringa = input()
		newstringa = ''
		for char in stringa:
			try:
				newchar = alpha[alpha.index(char)-indice]
			except:
				newchar = char
			newstringa += newchar
		print(newstringa)
			


os.system("clear")
ascii_art = pyfiglet.figlet_format("[tuxrs]")
        

console.print(f"[bold green]{ascii_art} [/bold green]")
        
startup_message = "welcome to tuxrs' cryptography toolkit."
startup_message2 = r"""choose an option 
[1] rot13 encryption
[2] secure password generator
[3] md5 cracker
[4] sha256,sha512 and sha1 generator

"""

print(startup_message)
time.sleep(1)
print(startup_message2)
scelta = int(input())

if scelta == 1:
    rot_13()

elif scelta == 2:
    pw_generatorr()

elif scelta == 3:
    hash_decryptor()

elif scelta == 4:
    startup_msg = r"""choose an option
[1] sha512 
[2] sha256 
[3] sha1"""
    print(startup_msg)
    sceltone = int(input())
    if sceltone == 1:
        sha512()
    elif sceltone == 2:
        sha256()
    elif sceltone == 3:
        sha1()


    
    

    
