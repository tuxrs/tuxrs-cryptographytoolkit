import time
import os 
import pyfiglet
from rich.console import Console
console = Console()





#!/usr/bin/python

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


    

    
