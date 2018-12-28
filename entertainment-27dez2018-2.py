# remove the date of the title for running

import media

toy_story = media.Movie("Toy Story",
						"A story of a boy...",
						"https://pt.wikipedia.org/wiki/Ficheiro:Avatar-Teaser-Poster.jpg",
						"https://www.youtube.com/watch?v=xy1ccIP_i24")

#print(toy_story.storyline)

avatar = media.Movie("Avatar",
					"A story of a marine...",
					"https://pt.wikipedia.org/wiki/Ficheiro:Avatar-Teaser-Poster.jpg",
					"https://www.youtube.com/watch?v=xy1ccIP_i24")

print(avatar.storyline)
avatar.show_trailer()