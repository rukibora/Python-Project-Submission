# Import necessary libraries
import pandas as pd  # For data manipulation and handling mappings
import tkinter as tk  # For creating the GUI (Graphical User Interface)
from tkinter import ttk, messagebox  # For additional widgets and message boxes
import requests  # To make HTTP requests to the OMDb API
import random  # For randomly selecting a movie from the list
from PIL import Image, ImageTk  # For handling image loading and resizing
from io import BytesIO  # For converting image data to a format suitable for Tkinter

# Define the API key for the OMDb API
API_KEY = "b81f1805"

# Function to recommend a movie based on user's input (mood, audience, and duration)
def suggest_movie():
    mood = mood_var.get()
    audience = audience_var.get()
    duration = duration_var.get()

    #Check if all fields are selected
    if not mood or not audience or not duration: #if one or more of the fields are not selected:
        messagebox.showwarning("Warning", "Please complete all selections above before getting a recommendation.")
        return
    
    # Define genre mappings based on mood and audience
    mood_genre_mapping = pd.DataFrame({
        "Happy": ["Comedy", "Family", "Animation", "Musical", "Adventure"],
        "Emotional": ["Drama", "Romance", "Family", "History", "War"],
        "Excited": ["Action", "Adventure", "Thriller", "Science Fiction", "Fantasy"],
        "Romantic": ["Romance", "Drama", "Fantasy", "Musical", "History"],
        "Adventurous": ["Adventure", "Action", "Crime", "Science Fiction", "Mystery"],
        "Funny": ["Comedy", "Family", "Animation", "Musical", "Adventure"],
        "Scared": ["Horror", "Thriller", "Mystery", "Crime", "War"],
        "Chill": ["Family", "Romance", "Comedy", "Fantasy", "Animation"],
        "Informed": ["History", "Documentary", "Biography", "Earth Science", "Short Film"]
    })

    audience_genre_mapping = pd.DataFrame({
        "With Family": ["Family", "Comedy", "Animation", "Adventure", "Musical"],
        "With Friends": ["Comedy", "Action", "Horror", "Science Fiction", "Thriller"],
        "With Partner": ["Romance", "Drama", "Comedy", "Musical", "Horror"],
        "Alone": ["Drama", "Mystery", "Fantasy", "Comedy", "Crime"],
    })

    # Fetch the genres corresponding to the selected mood and audience
    mood_genres = mood_genre_mapping.get(mood, [])
    audience_genres = audience_genre_mapping.get(audience, [])

   # Combine both mood and audience genres (removes duplicates) using Pandas
    selected_genre = pd.Series(list(set(mood_genres + audience_genres)))
    if len(selected_genre) > 5:
        selected_genre=selected_genre[:5]
    selected_duration = {
        "Short": 90,
        "Medium": 120,
        "Long": 150
    }[duration]

    # Form the URL to fetch movie data from the OMDb API based on the selected genres
    url = f"http://www.omdbapi.com/?apikey={API_KEY}&s=movie&type=movie&genre={','.join(selected_genre.dropna())}&page=10"
     
    # Make a request to the OMDb API
    response = requests.get(url)
    data = response.json()
    
    # Check if the response is valid (API returned movie data)
    if data.get("Response") == "True":
        # Filter movies based on the selected duration (only movies with a runtime <= selected duration)
        movies = [movie for movie in data["Search"] if int(movie.get("Runtime", "0").split()[0]) <= int(selected_duration)]

        # If there are movies matching the criteria, randomly select one
        if movies:
            selected_movie = random.choice(movies)
            title = selected_movie.get("Title")
            year = selected_movie.get("Year")
            poster_url = selected_movie.get("Poster")

            # Display the movie recommendation in the label on the GUI
            recommendation_label.config(text=f"You may enjoy:\n\n{title} ({year})")

            # Fetch the movie poster image from the URL
            response = requests.get(poster_url)
            img_data = response.content  # Get image data from the response
            img = Image.open(BytesIO(img_data)) # Open the image using PIL
            img = img.resize((200, 250), Image.Resampling.LANCZOS)  #Resize the image to fit the GUI layout

            # Convert the image into a format that Tkinter can display
            poster = ImageTk.PhotoImage(img)

            # Display the poster image on the GUI
            poster_label.config(image=poster)
            poster_label.image = poster  # Keep a reference to the image to prevent it from being garbage collected
        else:
            # If no movies were found, show an info message
            messagebox.showinfo("No Movies", "No movies found for the selected criteria.")
    else:
        # If there was an error with the API, show an error message
        messagebox.showinfo("API Error", "Unable to fetch movie data.")

# Set up the GUI window
root = tk.Tk()
root.title("Movie Recommender")  # Title of the window
root.geometry("450x700")  # Set the window size
root.configure(bg="DarkSeaGreen1")  # Set background color

# Create a label for the title at the top of the window
header_label = tk.Label(root, text="Movie Recommender", font=("Helvetica", 16, "bold"), bg="DarkSeaGreen1", fg="gray43")
header_label.grid(row=4, column=0, columnspan=2, pady=20)

# Create a label and dropdown for selecting mood (how the user wants to feel)
mood_label = ttk.Label(root, text="How do you want to feel?", background="DarkSeaGreen1", font=("Helvetica", 10), foreground="gray39")
mood_label.grid(row=5, column=0, sticky="w", padx=20, pady=10)
mood_var = tk.StringVar()
mood_options = ["Happy", "Emotional", "Excited", "Romantic", "Adventurous", "Funny", "Scared", "Chill", "Informed"]
mood_menu = ttk.Combobox(root, textvariable=mood_var, values=mood_options, width=20)
mood_menu.grid(row=5, column=1, padx=20, pady=10)

# Create a label and dropdown for selecting audience (with whom the user will watch the movie)
audience_label = ttk.Label(root, text="With whom will you watch the movie?", background="DarkSeaGreen1", font=("Helvetica", 10), foreground="gray39")
audience_label.grid(row=6, column=0, sticky="w", padx=20, pady=10)
audience_var = tk.StringVar()
audience_options = ["With Family", "With Friends", "With Partner", "Alone"]
audience_menu = ttk.Combobox(root, textvariable=audience_var, values=audience_options, width=20)
audience_menu.grid(row=6, column=1, padx=20, pady=10)

# Create a label and dropdown for selecting movie duration
duration_label = ttk.Label(root, text="Select Duration:", background="DarkSeaGreen1", font=("Helvetica", 10), foreground="gray39")
duration_label.grid(row=7, column=0, sticky="w", padx=20, pady=10)
duration_var = tk.StringVar()
duration_options = ["Short", "Medium", "Long"]
duration_menu = ttk.Combobox(root, textvariable=duration_var, values=duration_options, width=20)
duration_menu.grid(row=7, column=1, padx=20, pady=10)

# Create a button that will trigger the movie recommendation function
button = tk.Button(root, text="Get Recommendation", bg="sea green", fg="white", font=("Helvetica", 10), relief="raised", width=30, command=suggest_movie)
button.grid(row=8, column=0, columnspan=4, pady=20)

# Add a horizontal separator line between sections (for visuality)
separator = ttk.Separator(root, orient="horizontal")
separator.grid(row=9, column=0, columnspan=10, pady=10, sticky="ew")

# Create a frame to hold the movie recommendation and poster
recommendation_frame = tk.Frame(root, bg="DarkSeaGreen1")
recommendation_frame.grid(row=10, column=0, columnspan=3, pady=20)

# Label to display the movie recommendation
recommendation_label = tk.Label(recommendation_frame, text="", justify=tk.CENTER, bg="DarkSeaGreen1", font=("Helvetica", 10, "bold"), fg="gray20")
recommendation_label.grid(row=0, column=1, columnspan=3)

# Label to display the movie poster image
poster_label = tk.Label(recommendation_frame, justify=tk.CENTER, bg="DarkSeaGreen1")
poster_label.grid(row=1, column=1, columnspan=3)

# Run the Tkinter event loop to display the GUI and wait for user interactions
tk.mainloop()
