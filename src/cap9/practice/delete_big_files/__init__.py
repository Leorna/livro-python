import os
import time


def delete_big_files(path):
    if not os.path.exists(path):
        print('Path does not exist')
        return

    os.chdir(path)
    path = os.getcwd()
    MEGA = 10**6
    MAX_MB_SIZE = 10

    for folder, subfolders, files in os.walk(path):
        print(f'Current folder: {folder}')

        os.chdir(folder)

        for subfolder in subfolders:
            if os.path.getsize(subfolder) / MEGA > MAX_MB_SIZE:
                print(f'Deleting {subfolder}')

        for file in files:
            if os.path.getsize(file) / MEGA > MAX_MB_SIZE:
                print(f'Deleting {file}')

        print('----\n\n')
        os.chdir(path)
        #time.sleep(2)

    