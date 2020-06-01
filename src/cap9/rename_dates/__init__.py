#! python3.8

# módulo que renomeia arquivos com data no padrão estadunidense (MM-DD-AAAA) para o padrão europeu (DD-MM-AAAA)

import re
import os
import shutil


# regex que é o padrão de datas estadunidense
# ^(.*?) é qualquer palavra, frase no inicio do nome do arquivo
# ((0|1)?\d) representa o mês, que tem 0 ou 1 como começo do número e é opcional, \d representa qualquer digito de 0 a 9, Ex.: 12; 9, 01 
# - são separadores Ex.: 12-01-2002
# ((0|1|2|3)?\d) para representar o dia, regex análoga a regex que representa o mês, Ex.: 31, 01, 1
# ((19|20)?\d\d) representa o ano, digitos 19 e 20 são opcionais, Ex.: 2010, 10, 1989
# (.*?)$
data_pattern = re.compile(r"""
    ^(.*?)
    ((0|1)?\d)-
    ((0|1|2|3)?\d)-
    ((19|20)?\d\d)
    (.*?)$
""", re.VERBOSE)
