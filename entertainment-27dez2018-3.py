# remove the date of the title for running
import fresh_tomatoes
import media

toy_story = media.Movie("Toy Story",
						"A story of a boy...",
						"https://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",
						"https://www.youtube.com/watch?v=xy1ccIP_i24")

#print(toy_story.storyline)

avatar = media.Movie("Avatar",
					"A story of a marine...",
					"https://upload.wikimedia.org/wikipedia/pt/b/b0/Avatar-Teaser-Poster.jpg",
					"https://www.youtube.com/watch?v=xy1ccIP_i24")

#print(avatar.storyline)
#avatar.show_trailer()

o_leitor = media.Movie("O leitor",
					"A história de Michael Berg, um estudante alemão que, no ano de 1958, mantém um caso com uma mulher mais velha, Hanna Schmitz",
					"https://upload.wikimedia.org/wikipedia/en/6/6c/Reader_ver2.jpg",
					"https://www.youtube.com/watch?v=chcvR04q9Fw")

#o_leitor.show_trailer()

movies = [toy_story, avatar, o_leitor]

fresh_tomatoes.open_movies_page(movies)