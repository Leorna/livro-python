#! python3.8

# módulo que renomeia arquivos com data no padrão estadunidense (MM-DD-AAAA) para o padrão europeu (DD-MM-AAAA)

import re
import os
import shutil
import zipfile
import os
import time
import random


# regex que é o padrão de datas estadunidense
# ^(.*?) é qualquer palavra, frase no inicio do nome do arquivo
# ((0|1)?\d) representa o mês, que tem 0 ou 1 como começo do número e é opcional, \d representa qualquer digito de 0 a 9, Ex.: 12; 9, 01 
# - são separadores Ex.: 12-01-2002
# ((0|1|2|3)?\d) para representar o dia, regex análoga a regex que representa o mês, Ex.: 31, 01, 1
# ((19|20)?\d\d) representa o ano, digitos 19 e 20 são opcionais, Ex.: 2010, 10, 1989
# (.*?)$
date_pattern = re.compile(r"""
    ^(.*?)
    ((0|1)?\d)(-|/)
    ((0|1|2|3)?\d)(-|/)
    ((19|20)?\d\d)
    (.*?)$
""", re.VERBOSE)


def create_example_files():
    '''Cria arquivos com datas no padrão estadunidense'''
    random.seed(a=None)

    path = f'{os.getcwd()}/rename_dates'
    os.chdir(path)

    os.mkdir('example_files')
    os.chdir('./example_files')

    file = open('teste.txt', 'w')
    file.write('hello')
    file.close()

    for i in range(10):
        r_number = random.randint(0, 12)
        zip_file = zipfile.ZipFile(f'spam{i}-{i+1}-{i+r_number}-20{10+i}.zip', 'w')
        zip_file.write('teste.txt', compress_type=zipfile.ZIP_DEFLATED)

    os.unlink('./teste.txt')


def rename_dates():
    '''Renomeia arquivos com datas no estilo estadunidense para datas no estilo europeu'''
    try:
        create_example_files()
    except:
        if os.path.isdir('./example_files'):
            print('Files already exist')
            os.chdir('./example_files')
        else:
            raise Exception('Error unexpected')
    else:
        print('Files created')
        time.sleep(2)
    
    print('\nRenaming files...\n')
    
    for file_name in os.listdir('.'):
        mo = date_pattern.match(file_name)
        
        # Ignora os arquivos que nao tenham uma data
        if mo == None:
            continue
        
        # Obtem as diferentes partes do nome do arquivo
        before_part = mo.group(1)
        month_part = mo.group(2)
        day_part = mo.group(5)
        year_part = mo.group(8)
        after_part = mo.group(10)

        euro_file_name = f'{before_part}{day_part}-{month_part}-{year_part}{after_part}'
        
        abs_path = os.path.abspath('.')
        file_name = os.path.join(abs_path, file_name)
        euro_file_name = os.path.join(abs_path, euro_file_name)
       
        print(f'\n----{file_name} to {euro_file_name}----\n')
        shutil.move(file_name, euro_file_name)
        time.sleep(1)