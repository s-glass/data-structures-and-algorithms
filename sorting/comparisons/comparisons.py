from .movies import movies

# Movie class definition
class Movie:
    def __init__(self, title, year, genres):
        self.title = title
        self.year = year
        self.genres = genres

# Function to compare movies by most recent year first
def compare_by_year(movie1, movie2):
    return movie2.year - movie1.year

# Function to compare movies alphabetically, ignoring leading "A", "An", or "The"
def compare_alpha_titles(movie1, movie2):
    ignore_articles = ["A", "An", "The"]
    title1 = movie1.title.lstrip("AanThe ").lower()
    title2 = movie2.title.lstrip("AanThe ").lower()

    # If both titles are the same (ignoring articles), compare them using the original titles.
    if title1 == title2:
        return movie1.title < movie2.title

    return title1 < title2

# Sort movies by most recent year first
movies_sorted_by_year = sorted(movies, key=lambda movie: movie.year, reverse=True)
print("Movies sorted by most recent year first:")
for movie in movies_sorted_by_year:
    print(movie.title, movie.year)

# Sort movies alphabetically (ignoring articles)
movies_sorted_alphabetically = sorted(movies, cmp=compare_alpha_titles)
print("Movies sorted alphabetically (ignoring articles):")
for movie in movies_sorted_alphabetically:
    print(movie.title, movie.year)
