#import copy_files
#import os
from delete_big_files import delete_big_files

def main():
    #copy_files.copy_files(os.getcwd(), '/home/gabriel/Documentos')
    delete_big_files('/home/gabriel')


if __name__ == '__main__':
    main()