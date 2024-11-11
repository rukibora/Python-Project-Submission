import requests
import random
import csv
import pandas as pd

valid_genres = ['action', 'comedy', 'drama', 'horror', 'romance', 'thriller', 'sci-fi', 'fantasy']

def get_movies(genre):
    url = f'https://www.omdbapi.com/?s={genre}&apikey=b81f1805'
    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()
        if data.get('Response') == 'True':
            return data['Search']
        else:
            print(f"No movies found for the genre {genre}.")
            return []
    else:
        print(f"Error fetching data for genre {genre}. Status code: {response.status_code}")
        return []

def save_movies_to_csv(movies, genre):
    movie_data = []
    for movie in movies:
        movie_data.append([movie['Title'], movie['Year'], movie['imdbID']])

    df = pd.DataFrame(movie_data, columns=['Title', 'Year', 'IMDB ID'])

    df.to_csv(f'{genre}_movies.csv', index=False, encoding='utf-8')
    print(f"Movies saved to {genre}_movies.csv.")

def recommend_random_movie(movies):
    if movies:
        random_movie = random.choice(movies)
        print(f"\nRecommended Movie: {random_movie['Title']} ({random_movie['Year']})")
        
    else:
        print("No movies to recommend.")

def main():
    while True:
        genre = input("Please enter a movie genre (e.g., action, comedy, drama): ").strip().lower()

        if genre not in valid_genres:
            print("Unknown genre. Please choose a valid genre.")
            continue
        
        print(f"{genre} movies are being fetched...")
        movies = get_movies(genre)
        
        if movies:
            save_movies_to_csv(movies, genre)
            recommend_random_movie(movies)
            break

if __name__ == "__main__":
    main()