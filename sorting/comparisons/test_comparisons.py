# Test both comparator functions
from .movies import movies
from .comparisons import compare_by_year, compare_alpha_titles

# Test compare_by_year
movies_sorted_by_year = sorted(movies, key=lambda movie: movie.year, reverse=True)
expected_by_year = [
    "The Intouchables", "Valkyrie", "Stardust", "Ratatouille", "City of God",
    "Memento", "The Shawshank Redemption", "Beetlejuice", "Crocodile Dundee", "The Cotton Club"
]

assert [movie.title for movie in movies_sorted_by_year] == expected_by_year

# Test compare_alpha_titles
movies_sorted_alphabetically = sorted(movies, cmp=compare_alpha_titles)
expected_alphabetically = [
    "Beetlejuice", "City of God", "The Cotton Club", "Crocodile Dundee",
    "The Intouchables", "Memento", "Ratatouille", "The Shawshank Redemption", "Stardust", "Valkyrie"
]

assert [movie.title for movie in movies_sorted_alphabetically] == expected_alphabetically

# Output success message if all tests pass
print("All tests passed!")
