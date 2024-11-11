# Python-Project-Submission
Movie Recommender App

This Python project is a movie recommender application. The app allows users to input a movie genre (such as action, comedy, drama, etc.), fetches movie data from the OMDB API, saves the data into a CSV file using Pandas, and recommends 1 random movie from the selected genre. Each recommended movie is provided with its year of release.

Features

User Input: Users can input a movie genre (e.g., action, comedy, drama).
Data Fetching: The app fetches movie data using the OMDB API.
CSV Saving with Pandas: The fetched movie data is saved in a CSV file using the Pandas library for better data manipulation.
Movie Recommendation: The app randomly selects 1 movie from the fetched list and displays it with its year of release.
Error Handling: The app handles cases like invalid genres and failed data fetching gracefully.


Requirements

This project requires the following Python libraries:
requests: For making HTTP requests to the OMDB API.
random: For selecting random movies.
pandas: For saving the fetched movie data into a CSV file and performing data manipulations.


Install the required libraries:

You can install the required libraries using pip:
pip install requests pandas

Setup

1. Clone or download the repository to your local machine.
2. Open the project folder in your terminal or command prompt.
3. Create a Python script (e.g., movie_picker.py).
4. Copy and paste the provided Python code into your script.



OMDB API Key

To use the OMDB API, you'll need an API key. You can get a free API key by registering on the OMDB API website.
Once you have your API key, replace b81f1805 in the code with your own API key.

How It Works

1. Input Genre: The user is prompted to input a movie genre (e.g., action, comedy, drama).
2. Fetch Movies: The app sends a request to the OMDB API to get a list of movies for the given genre.
3. Save Data with Pandas: The fetched movie data is saved into a CSV file named <genre>_movies.csv, containing the title, year, and IMDb ID of each movie. Pandas is used to handle data and write it to CSV for efficiency and easy management.
4. Recommend Movie: The app selects 1 random movie from the fetched list using the random library and displays the title and the year of the picked movie.

Example Usage

Please enter a movie genre (e.g., action, comedy, drama): comedy
comedy movies are being fetched...

Movies saved to comedy_movies.csv.

Here is your movie recommendation:
The Hangover (2009)
   

Files Generated

The app generates a CSV file named <genre>_movies.csv that contains the movie data with the following columns:
Title: The title of the movie.
Year: The release year of the movie.
IMDB ID: The IMDb ID of the parsed movies.


Example of CSV file (comedy_movies.csv):

Title,Year,IMDB ID
The King of Comedy,1982,tt0085794
Fear City: A Family-Style Comedy,1994,tt0109440
The Broken Hearts Club: A Romantic Comedy,2000,tt0222850
...

Why Pandas?

Pandas is used in this project for the following reasons:
1. Efficient Data Handling: With Pandas, we can easily manipulate and manage data, such as cleaning, filtering, and transforming.
2. CSV Handling: Pandas provides a simple and efficient way to save data into CSV files using to_csv(), ensuring the data is well-organized and easy to manage.
3. Dataframe Structure: Using Pandas allows us to organize movie data into a structured dataframe, making it easy to perform operations like sorting or filtering in the future.

Error Handling

Invalid Genre: If the user enters a genre that is not supported, the app will print a message asking the user to choose a valid genre.
API Request Failure: If the API request fails (e.g., due to network issues or invalid API key), the app will notify the user of the error.

Known Issues

If the OMDB API limit is exceeded (in case of multiple requests within a short period), the app may not be able to fetch new data. You can wait for a while or upgrade to a premium API key for higher limits.
The app currently supports a limited number of genres. To extend the functionality, you can update the list of valid genres.

Future Enhancements:

Implement multiple API support (e.g., support for both OMDb and TMDb).
Add more advanced user inputs (e.g., multiple genres, movie rating filters).
Enhance the movie suggestion algorithm (e.g., based on movie ratings or year).

License

This project is open-source and available under the MIT License.


---

Notes:

Ensure your API key is correctly placed in the code before running it.
The project will generate a CSV file in the working directory for each genre you choose.


