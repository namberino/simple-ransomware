#!/usr/local/bin/python3 

import os
from cryptography.fernet import Fernet

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

with open(".a_deal", "rb") as deal:
	key = deal.read()

for file in files:
	with open(file, "rb") as f:
		content = f.read()

	content_decrypted = Fernet(key).decrypt(content)

	with open(file, "wb") as f:
		f.write(content_decrypted)

print("Files decrypted!")
