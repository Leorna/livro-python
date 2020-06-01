import os

#   string       list        list
for folder_name, subfolders, filenames in os.walk('/home/gabriel/delicious'):
    print(f'The current folder is {folder_name}')

    for subfolder in subfolders:
        print(f'Subfolder of {folder_name}: {subfolder}')

    for filename in filenames:
        print(f'File inside {folder_name}: {filename}')

    print('')