# 🎬 RecomAI — AI Movie Recommendation System

RecomAI is a simple movie recommendation system developed as part of the DecodeLabs Industrial Training Kit 2026 — Project 3: **AI Recommendation Logic**.

The system recommends movies based on a user's selected preferences and uses a similarity-based matching approach to rank the most relevant movies.

---

## 📌 Project Overview

RecomAI takes four user preferences:

- Genre
- Language
- Mood
- Type

It compares these preferences with the attributes of available movies and calculates a similarity score.

Each matching attribute contributes equally to the final score.

The system then ranks the movies according to their similarity scores and displays the top 3 recommendations.

---

## ✨ Features

- 🎯 Preference-based movie recommendations
- 🧠 Similarity-based recommendation logic
- 📊 Percentage match scores
- 📈 Visual match bars
- ✅ Shows which attributes matched
- ❌ Shows which attributes did not match
- 🖥️ Simple and responsive web interface
- ⚡ Real-time recommendations without reloading the page

---

## 🧠 How the Recommendation Logic Works

RecomAI compares the user's preferences with four movie attributes:

1. Genre
2. Language
3. Mood
4. Type

Each attribute has equal importance.

There are four attributes in total, so:

- **1 matching attribute = 25%**
- **2 matching attributes = 50%**
- **3 matching attributes = 75%**
- **4 matching attributes = 100%**

### Similarity Formula

Similarity Score = (Number of Matching Attributes / Total Attributes) × 100

For example, if a user's preferences match a movie in 3 out of 4 attributes:

(3 / 4) × 100 = 75%

The movies are then sorted from the highest similarity score to the lowest, and the top 3 are displayed.

---

## 🛠️ Technologies Used

- Python
- Flask
- HTML
- CSS
- JavaScript

---

## 📂 Project Structure

decodelabs-project-3/
│
├── recommender/
│   └── recommendation.py
│
├── templates/
│   └── index.html
│
├── static/
│   ├── style.css
│   └── script.js
│
├── app.py
├── requirements.txt
└── README.md

---

## 🚀 How to Run the Project

### 1. Clone the repository

git clone <repository-url>

### 2. Open the project directory

cd decodelabs-project-3

### 3. Create a virtual environment

python -m venv venv

### 4. Activate the virtual environment

Windows:

venv\Scripts\activate

### 5. Install the required dependencies

pip install -r requirements.txt

### 6. Run the Flask application

python app.py

### 7. Open the application

Open the following address in a web browser:

http://127.0.0.1:5000

---

## 🎬 Example

If a user selects:

Genre: Sci-Fi
Language: English
Mood: Thought-provoking
Type: Movie

The system identifies **Interstellar** as a 100% match because all four attributes match the user's preferences.

Other movies are assigned scores according to the number of matching attributes.

---

## 📋 Available Movies

The current recommendation dataset contains:

- Interstellar
- Inception
- The Martian
- The Notebook
- La La Land
- 3 Idiots
- Zindagi Na Milegi Dobara
- The Pursuit of Happyness

---

## 🎯 Project Objective

The objective of this project is to demonstrate fundamental recommendation-system concepts through:

- User preference collection
- Logic-based matching
- Similarity scoring
- Ranking recommendations
- Displaying relevant recommendations to the user

The system uses a straightforward similarity approach rather than a trained machine-learning or deep-learning model.

---

## 👩‍💻 Developed For

**DecodeLabs Industrial Training Kit 2026**

**Project 3 — AI Recommendation Logic**

---

## 🔮 Future Improvements

Possible future improvements include:

- Adding more movies and attributes
- Allowing users to rate movies
- Using weighted similarity scores
- Adding movie posters and additional metadata
- Using larger datasets
- Exploring more advanced recommendation algorithms

---

## 📄 License

This project was developed for educational and internship purposes.
