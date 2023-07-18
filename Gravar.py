arquivo = open('arqText.txt', 'w')

arquivo.write('Curso Python \n')
arquivo.write('Aula Prática')
arquivo.close()

#Leitura do arquivo de texto

leitura = open('arqText.txt', 'r')
print(leitura.read())
leitura.close()