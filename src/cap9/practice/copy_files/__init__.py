import os
import shutil
import time


def copy_files(path, destiny,  *ends_of_file):
    if not os.path.exists(path) or not os.path.exists(destiny):
        print('Path does not exist!')
        return

    try:
        print('Creating copied folder...')
        os.makedirs(f'{destiny}/copied')
    except:
        print('Folder alread created')
    else:
        print('Folder created')
    

    time.sleep(2)

    copied_folder_path = os.path.join(os.path.abspath(destiny), 'copied')
    
    print(f'\n----Coping files in {path} to {copied_folder_path}----\n')
    for file in os.listdir(path):
        if len(ends_of_file):
            for end_of_file in ends_of_file:
                if file.endswith(end_of_file) and os.path.isfile(file):
                    print(f'Coping {file}')
                    shutil.copy(os.path.join(path, file), copied_folder_path)
                    time.sleep(2)
        elif os.path.isfile(file):
            print(f'Coping {file}')
            shutil.copy(os.path.join(path, file), copied_folder_path)
            time.sleep(2)
   