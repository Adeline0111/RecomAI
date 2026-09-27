# Movie dataset for RecomAI

movies = [
    {
        "title": "Interstellar",
        "genre": "Sci-Fi",
        "language": "English",
        "mood": "Thought-provoking",
        "type": "Movie"
    },
    {
        "title": "Inception",
        "genre": "Sci-Fi",
        "language": "English",
        "mood": "Thrilling",
        "type": "Movie"
    },
    {
        "title": "The Martian",
        "genre": "Sci-Fi",
        "language": "English",
        "mood": "Inspirational",
        "type": "Movie"
    },
    {
        "title": "The Notebook",
        "genre": "Romance",
        "language": "English",
        "mood": "Emotional",
        "type": "Movie"
    },
    {
        "title": "La La Land",
        "genre": "Romance",
        "language": "English",
        "mood": "Feel-Good",
        "type": "Movie"
    },
    {
        "title": "3 Idiots",
        "genre": "Comedy",
        "language": "Hindi",
        "mood": "Inspirational",
        "type": "Movie"
    },
    {
        "title": "Zindagi Na Milegi Dobara",
        "genre": "Drama",
        "language": "Hindi",
        "mood": "Feel-Good",
        "type": "Movie"
    },
    {
        "title": "The Pursuit of Happyness",
        "genre": "Drama",
        "language": "English",
        "mood": "Inspirational",
        "type": "Movie"
    }
]
def calculate_similarity(user_preferences, movie):
    """
    Calculate how closely a movie matches the user's preferences.
    Each matching preference contributes equally to the score.
    """

    attributes = ["genre", "language", "mood", "type"]

    matches = []
    mismatches = []

    for attribute in attributes:
        if user_preferences[attribute] == movie[attribute]:
            matches.append(attribute)
        else:
            mismatches.append(attribute)

    score = (len(matches) / len(attributes)) * 100

    return score, matches, mismatches

def get_recommendations(user_preferences, number_of_recommendations=3):
    """
    Generate movie recommendations based on similarity scores.
    """

    recommendations = []

    for movie in movies:
        score, matches, mismatches = calculate_similarity(
            user_preferences,
            movie
        )

        recommendations.append({
            "title": movie["title"],
            "score": score,
            "matches": matches,
            "mismatches": mismatches,
            "movie": movie
        })

    # Sort movies from highest score to lowest score
    recommendations.sort(
        key=lambda recommendation: recommendation["score"],
        reverse=True
    )

    return recommendations[:number_of_recommendations]

    # Sort movies from highest score to lowest score
    recommendations.sort(
        key=lambda recommendation: recommendation["score"],
        reverse=True
    )

    return recommendations[:number_of_recommendations]    


