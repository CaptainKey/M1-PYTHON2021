import os 

directory = 'POO/'
directory = 'undossier/'

exist = os.path.exists(directory)
if exist:
    print('OK')
else:
    os.makedirs(directory)