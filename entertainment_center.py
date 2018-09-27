import media
import fresh_tomatoes

bourne = media.Movie("Bourne identity",
                        "Man with amnesia finds out he's a super guy",
                        "https://upload.wikimedia.org/wikipedia/id/a/ae/BourneIdentityfilm.jpg",
                        "https://www.youtube.com/watch?v=AfkNq0CDx6w")


matrix = media.Movie("matrix",
                     "red pill or blue pill",
                     "https://upload.wikimedia.org/wikipedia/sco/c/c1/The_Matrix_Poster.jpg",
                     "https://www.youtube.com/watch?v=m8e-FF8MsqU")

dumb = media.Movie("Dumb and Dumber",
                   "Two dumb guys do dumb things",
                   "https://upload.wikimedia.org/wikipedia/fi/5/5b/Dumb-and-dumber-poster.jpg",
                   "https://www.youtube.com/watch?v=l13yPhimE3o")


movies = [bourne,matrix,dumb]
#fresh_tomatoes.open_movies_page(movies)
print("name : " + media.Movie.__name__)
print("module : " + media.Movie.__module__)
