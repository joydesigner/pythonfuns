from bs4 import BeautifulSoup
import requests

# URL of the webpage to scrape
URL = 'https://www.empireonline.com/movies/features/best-movies-2/'

# File to save the movies
OUTPUT_FILENAME = 'movies.txt'

def fetch_movie_titles(url):
    """Fetches movie titles from the given URL."""
    try:
        response = requests.get(url)
        response.raise_for_status() # Raise HTTPError for bad responses
        soup = BeautifulSoup(response.text, 'html.parser')

        #Extract movie titles
        return [movie.getText() for movie in soup.findAll(name='h3', class_='listicleItem_listicle-item__title__BfenH')]
    except requests.exceptions.RequestException as e:
        print(f'Error fetching the webpage: {e}')
        return []

def save_movies_to_file(movies, filename):
    """Saves the list of movies to a file in reversed order."""
    try:
        with open(filename, 'w') as file:
            for index, movie in enumerate(movies, start=1):
                file.write(f'{movie}\n')
        print(f'Movies saved to {filename} successfully!')
    except IOError as e:
        print(f'Error writing to file: {e}')

def main():
    # Fetch and process movie titles
    print('Fetching movie titles...')
    movies = fetch_movie_titles(URL)

    if movies:
        # Reverse the movie list
        print('Reversing movie list...')
        movies.reverse()

        # Save to file
        save_movies_to_file(movies, OUTPUT_FILENAME)
    else:
        print('No movies to save. Exiting.')

if __name__ == '__main__':
    main()


