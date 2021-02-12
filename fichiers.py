file = open('monfichier.txt','w')
file.write('Coucou')
file.close()

file = open('monfichier.txt','r')
print(file.read())
