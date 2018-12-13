with open("movie_quotes.txt") as f:
    lines = f.read().splitlines()
    print(lines)
    tamanho = len(lines)
    print(tamanho)