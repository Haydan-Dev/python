# READING AND WRITING A FILE
# 'r+' mode allows both reading and writing
f = open('ExeptionHandling.py', 'r+') 

text = f.read()
f.write('\n# This is file handling testing in this file, by me haydan') 

print("Purana File Data:", text)
print("File successfully updated! ")

f.close()