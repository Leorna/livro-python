import zipfile
import os


def backup_to_zip(folder):
    folder = os.path,abspath(folder)

    number = 1

    while True:
        zip_file_name = os.path.basename(folder) + '_' + str(number) + '.zip'

        if not os.path.exists(zip_file_name):
            break

        number += 1

        