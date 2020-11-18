class Painting:
    place = "Louvre"

    def __init__(self, title, artist, year):
        self.title = title
        self.artist = artist
        self.year = year

    def get_info(self):
        print(f'"{self.title}" by {self.artist} ({self.year}) hangs in the {Painting.place}.')


painting = Painting(input(), input(), input())
painting.get_info()