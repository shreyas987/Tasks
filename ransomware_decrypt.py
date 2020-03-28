import os
import base64
import math


def decrypt_msg(KEY,MSG):
    MSG = "" 
  
    # track key indices 
    k_indx = 0
  
    # track msg indices 
    msg_indx = 0
    msg_len = float(len(ciphertext)) 
    msg_lst = list(ciphertext) 
  
    # calculate column of the matrix 
    col = len(KEY) 
      
    # calculate maximum row of the matrix 
    row = int(math.ceil(msg_len / col)) 
  
    # convert key into list and sort
    key_lst = sorted(list(KEY)) 
  
    # create an empty matrix to   
    dec_cipher = [] 
    for _ in range(row): 
        dec_cipher += [[None] * col] 
  
    # Arrange the matrix column wise according  
    for _ in range(col): 
        curr_idx = KEY.index(key_lst[k_indx]) 
  
        for j in range(row): 
            dec_cipher[j][curr_idx] = msg_lst[msg_indx] 
            msg_indx += 1
        k_indx += 1
  
    # convert decrypted msg matrix into a string 
    try: 
        MSG = ''.join(sum(dec_cipher, [])) 
    except TypeError: 
        raise TypeError("This program cannot", "handle repeating words.") 
  
    null_count = MSG.count('*') 
  
    if null_count > 0: 
        return MSG[: -null_count] 
  
    return MSG 


KEY = "BITS"
path = '/home/shreyas/Desktop/Sem2/ns/Ransomware/test'

fileList = os.listdir(path)
for i in fileList:
	#if (i.endswith('.jpg') or i.endswith('.jpeg') or i.endswith('.png')):
	#	f=open(os.path.join(path,i), "r")
	#	imgdata = base64.b64decode(f.read())
	#	#filename = 'some_image.jpg'  # I assume you have a way of picking unique filenames
	#	with open(i, 'wb') as img:
    	#		img.write(imgdata)	
	#else:
		f=open(os.path.join(path,i), "r")
        
		plaintext = ""
		ciphertext = f.read()
		plaintext = decrypt_msg(KEY,ciphertext)
	
        	f=open(os.path.join(path,i), "w+")
		f.write(plaintext)



