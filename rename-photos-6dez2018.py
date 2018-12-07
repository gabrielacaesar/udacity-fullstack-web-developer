# item 21 da aula 5
# objetivo: temos uma pasta com 50 fotos
# queremos renomear todos os arquivos
# e, assim, tirar todos os números desses nomes

# os.listdir() te dá tudo que há dentro de um diretório
# translate mudou de python 2 para python 3

import os
def rename_files():
	file_list = os.listdir("../Downloads/prank")
	#print(file_list)
	saved_path = os.getcwd()
	print("current working directory is " + saved_path)
	os.chdir("../Downloads/prank")

	for file_name in file_list:
		numbers = str.maketrans(dict.fromkeys('0123456789'))
		os.rename(file_name, file_name.translate(numbers))
	os.chdir(saved_path)

rename_files()