import webbrowser


class Movie():
    """Movie class

    Attributes:
        title: movie title
        storyline: movie storyline description
        poster_image_url: movie poster image
        trailer_youtube_url: link to movie trailer video
    """
    # constructor
    def __init__(self,
                 title,
                 storyline,
                 poster_image_url,
                 trailer_youtube_url):
        self.title = title
        self.storyline = storyline
        self.poster_image_url = poster_image_url
        self.trailer_youtube_url = trailer_youtube_url
