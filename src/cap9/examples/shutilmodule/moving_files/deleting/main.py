import os
import time

os.chdir('/home/gabriel')

print(os.getcwd())

for filename in os.listdir():
    if filename.endswith('.rxt'):
        print(f'Deleting {filename}')
        
        os.unlink(filename)

        time.sleep(1)