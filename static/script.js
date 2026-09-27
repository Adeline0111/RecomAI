const recommendButton = document.getElementById("recommendButton");
const resultsContainer = document.getElementById("results");

recommendButton.addEventListener("click", async () => {

    const userPreferences = {
        genre: document.getElementById("genre").value,
        language: document.getElementById("language").value,
        mood: document.getElementById("mood").value,
        type: document.getElementById("type").value
    };

    try {

        const response = await fetch("/recommend", {
            method: "POST",

            headers: {
                "Content-Type": "application/json"
            },

            body: JSON.stringify(userPreferences)
        });

        const recommendations = await response.json();

        displayRecommendations(recommendations);

    } catch (error) {

        console.error("Error:", error);

        resultsContainer.innerHTML =
            "<p>Something went wrong. Please try again.</p>";
    }
});


function displayRecommendations(recommendations) {

    resultsContainer.innerHTML = "";

    recommendations.forEach(recommendation => {

        const movieCard = document.createElement("div");

        movieCard.className = "movie-card";

       const attributeNames = {
    genre: "Genre",
    language: "Language",
    mood: "Mood",
    type: "Type"
};

movieCard.innerHTML = `
    <h3>🎬 ${recommendation.title}</h3>

    <div class="match-score">
        ${recommendation.score}% Match
    </div>

    <div class="match-bar">
        <div class="match-fill" style="width: ${recommendation.score}%"></div>
    </div>

    <p class="why-title">Why this matches</p>

    <ul class="match-list">

        ${recommendation.matches.map(attribute =>
            `<li class="matched">✓ ${attributeNames[attribute]}</li>`
        ).join("")}

        ${recommendation.mismatches.map(attribute =>
            `<li class="not-matched">✗ ${attributeNames[attribute]}</li>`
        ).join("")}

    </ul>
`;

        resultsContainer.appendChild(movieCard);
    });
}