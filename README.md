Movie Recommender Application

Overview

The Movie Recommender application is a simple GUI-based tool built using Python's Tkinter library, which allows users to get personalized movie recommendations based on their mood, the audience they'll be watching with, and the preferred movie duration. The application interacts with the OMDb API to fetch movie data, such as titles, release years, posters, and runtime details, and then recommends a movie based on the user's inputs.

Currently, the application uses a free OMDb API to fetch movie information. In future updates, I aim to expand the tool to incorporate a paid API that provides keyword-based movie data tailored to selected audience types, allowing for even more personalized recommendations.

Features

Mood-Based Movie Recommendations: Users can choose their mood, such as "Happy", "Excited", "Romantic", etc., which influences the genres of movies recommended.

Audience-Based Filters: The user selects with whom they will watch the movie (Family, Friends, Partner, or Alone), which further refines the movie suggestions based on suitable genres for each audience type.

Movie Duration Filter: The application allows users to choose the length of the movie they prefer (Short, Medium, or Long), filtering out movies that do not match the selected runtime.

Movie Posters and Titles: Along with the movie title and year, the app displays a movie poster for visual reference.

User-Friendly GUI: Built with Tkinter, the application is equipped with a simple interface to facilitate ease of use.

Current API Setup

The movie data is fetched using the OMDb API. The following parameters are used to request movie data:

Mood: Selected moods influence the genres of movies recommended.
Audience: Whether the user is watching alone, with family, friends, or a partner, the genre filters are adjusted.
Duration: Users can filter movies by their runtime (Short, Medium, or Long).

The movie data is fetched by making an HTTP request to the OMDb API, using the following endpoint:
http://www.omdbapi.com/?apikey={API_KEY}&s=movie&type=movie&genre={selected_genre}&page=10

The application then filters out movies that don't meet the selected duration criteria and randomly selects one movie to display.

Future Enhancements

Paid API Integration: In future versions, I plan to integrate a paid API that offers more advanced features, such as keyword-based movie recommendations tailored to specific audiences. This will allow for more precise movie suggestions based on detailed user preferences.

Advanced Recommendation Algorithms: The system may incorporate machine learning or additional user inputs to improve the accuracy and personalization of movie suggestions.

Dependencies

The application uses the following Python libraries:

pandas: For data manipulation and handling genre mappings.

tkinter: For creating the graphical user interface.

requests: To make HTTP requests to the OMDb API.

PIL (Pillow): For handling image loading and resizing of movie posters.

random: For randomly selecting a movie from the fetched list.

io: To handle image data in a format suitable for Tkinter.


Ensure that you have the necessary dependencies installed:

pip install pandas requests pillow

Usage

1. Select Mood: Choose how you want to feel from options like Happy, Excited, etc.
2. Select Audience: Choose whether you're watching with Family, Friends, Partner, or Alone.
3. Select Duration: Pick the preferred duration (Short, Medium, or Long).
4. Get Recommendation: Click the "Get Recommendation" button to receive a movie suggestion.

The selected movie’s title, year, and poster will be displayed within the app.

License

This project is open-source and available under the MIT License. Feel free to contribute to its development or use it as a base for further enhancements.

Contact

For questions or feedback, feel free to reach out.
