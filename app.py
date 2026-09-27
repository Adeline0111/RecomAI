from flask import Flask, render_template, request, jsonify
from recommender.recommendation import get_recommendations

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/recommend", methods=["POST"])
def recommend():
    data = request.get_json()

    user_preferences = {
        "genre": data["genre"],
        "language": data["language"],
        "mood": data["mood"],
        "type": data["type"]
    }

    recommendations = get_recommendations(user_preferences)

    return jsonify(recommendations)


if __name__ == "__main__":
    app.run(debug=True)