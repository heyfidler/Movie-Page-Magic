import media
import fresh_tomatoes

# build movie objects
bourne = media.Movie("Bourne Identity",
                     "A man with memory loss tries to find his identity",
                     "https://upload.wikimedia.org/wikipedia/id/a/ae/BourneIdentityfilm.jpg",  # NOQA
                     "https://www.youtube.com/watch?v=FpKaB5dvQ4g")

matrix = media.Movie("Matrix",
                     "A man wakes up to the real world",
                     "https://upload.wikimedia.org/wikipedia/sco/c/c1/The_Matrix_Poster.jpg",  # NOQA
                     "https://www.youtube.com/watch?v=m8e-FF8MsqU")

dumb = media.Movie("Dumb and Dumber",
                   "Two dumb guys do dumb things",
                   "https://upload.wikimedia.org/wikipedia/fi/5/5b/Dumb-and-dumber-poster.jpg",  # NOQA
                   "https://www.youtube.com/watch?v=l13yPhimE3o")

top_gun = media.Movie("Top Gun",
                      "A Navy pilot joins elite fighter school",
                      "https://upload.wikimedia.org/wikipedia/en/4/46/Top_Gun_Movie.jpg",  # NOQA
                      "https://www.youtube.com/watch?v=xa_z57UatDY")

in_bruges = media.Movie("In Bruges",
                        "Two Irish hitmen wait for their boss in Bruges",
                        "https://upload.wikimedia.org/wikipedia/en/e/ee/In_Bruges_poster.png",  # NOQA
                        "https://www.youtube.com/watch?v=96harmMOyiY")

casino_royale = media.Movie("Casino Royale",
                            "James Bond before he had a license to kill",
                            "https://imgc.allpostersimages.com/img/print/u-g-F5UZ430.jpg?w=900&h=900&p=0",  # NOQA
                            "https://www.youtube.com/watch?v=fl5WHj0bZ2Q")

# build array of movie objects for argument to open_movies_page
movies = [bourne, matrix, dumb, top_gun, in_bruges, casino_royale]

# build movie html page and open in browser
fresh_tomatoes.open_movies_page(movies)