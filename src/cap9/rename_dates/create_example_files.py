import zipfile
import os


def create_example_files():
    '''Cria arquivos com datas no padrão estadunidense'''
    path = f'{os.getcwd()}/rename_dates'
    os.chdir(path)

    os.mkdir('example_files')
    os.chdir('./example_files')

    file = open('teste.txt', 'w')
    file.write('hello')
    file.close()

    for i in range(10):
        zip_file = zipfile.ZipFile(f'spam(MM-DD-AAAA){i+1}-{i+1}-20{10+i}.zip', 'w')
        zip_file.write('teste.txt', compress_type=zipfile.ZIP_DEFLATED)

    os.unlink('./teste.txt')
