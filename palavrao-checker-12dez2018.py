## Nao rodou porque houve uma mudanca na biblioteca
## do Python 2 para o Python 3

from urllib.request import urlopen

def read_text():
	quotes = open("movie_quotes.txt")
	contents_of_file = quotes.read()
	print(contents_of_file)
	quotes.close()
	check_profanity(contents_of_file)


def check_profanity(text_to_check):
	connection = urllib.request.urlopen("http://www.wdylike.appspot.com/?q=" + text_to_check)
	output = connection.read()
	print(output)
	connection.close()

read_text()


