import os

source = 'main.txt'
dest = 'newfile.txt'
os.rename(source,dest)
print("Source Path renamed to destination path successfully")