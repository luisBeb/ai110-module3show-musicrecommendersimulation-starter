# 🎵 Music Recommender Simulation

## Project Summary

My version is a small content-based music recommender written in Python. It loads a
catalog of songs from a CSV file, compares each song's attributes (genre, mood, and
energy) against a user's taste profile, and gives each song a weighted score. It then
ranks all the songs by score and prints the top recommendations in the terminal,
along with the reasons each song earned points.

---

## How The System Works

Real-world platforms like Spotify predict what users will love using two main
approaches: collaborative filtering (recommending songs based on the behavior of
users with similar taste) and content-based filtering (recommending songs whose
attributes match the user's taste profile). Big platforms blend both, using data
like likes, skips, playlists, tempo, and mood. My version is a simplified
content-based recommender, since it only uses song attributes and not other users'
behavior.

- **Song features used:** genre, mood, energy
- **UserProfile stores:** favorite_genre, favorite_mood, target_energy
- **Scoring:** a song earns +2.0 points for matching the favorite genre, +1.0 for
  matching the favorite mood, and similarity points based on how close its energy
  is to the user's target energy (closer = more points).
- **Choosing recommendations:** every song in the catalog gets scored, the list is
  sorted from highest to lowest, and the top k songs are recommended.

---

## Getting Started

### Setup

1. Create a virtual environment (optional but recommended):

```bash
   python -m venv .venv
   source .venv/bin/activate      # Mac or Linux
   .venv\Scripts\activate         # Windows
```

2. Install dependencies:

```bash
   pip install -r requirements.txt
```

3. Run the app:

```bash
   python -m src.main
```

### Running Tests

Run the starter tests with:

```bash
pytest
```

You can add more tests in `tests/test_recommender.py`.

---

## Sample Recommendation Output

```
Loaded songs: 18

User profile: genre=pop, mood=happy, energy=0.8

Top recommendations:

  1. Sunrise City — Neon Echo  (Score: 3.98)
     Because: genre match (+2.0), mood match (+1.0), energy similarity (+0.98)

  2. Gym Hero — Max Pulse  (Score: 2.87)
     Because: genre match (+2.0), energy similarity (+0.87)

  3. Rooftop Lights — Indigo Parade  (Score: 1.96)
     Because: mood match (+1.0), energy similarity (+0.96)

  4. Isla Bonita Nights — Sabor Urbano  (Score: 1.95)
     Because: mood match (+1.0), energy similarity (+0.95)

  5. Night Drive Loop — Neon Echo  (Score: 0.95)
     Because: energy similarity (+0.95)
```

---

## Experiments You Tried

Use this section to document the experiments you ran. For example:

- What happened when you changed the weight on genre from 2.0 to 0.5
- What happened when you added tempo or valence to the score
- How did your system behave for different types of users

---

## Limitations and Risks

Summarize some limitations of your recommender.

Examples:

- It only works on a tiny catalog
- It does not understand lyrics or language
- It might over favor one genre or mood

You will go deeper on this in your model card.

---

## Reflection

Read and complete `model_card.md`:

[**Model Card**](model_card.md)

Write 1 to 2 paragraphs here about what you learned:

- about how recommenders turn data into predictions
- about where bias or unfairness could show up in systems like this



