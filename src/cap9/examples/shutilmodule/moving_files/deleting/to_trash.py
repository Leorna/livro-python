import send2trash as s2t
import os


os.chdir('/home/gabriel')


try:
    s2t.send2trash('./teste')
except:
    print('File does not exist')
else:
    print('File sent to trash')

