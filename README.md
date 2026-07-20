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

**Weight Shift experiment:** I halved the genre weight (2.0 → 1.0) and doubled the
energy weight (max 1.0 → max 2.0), keeping the maximum score at 4.0 so results
stayed comparable. The top recommendation for each profile barely changed, but the
score gaps compressed a lot: for the High-Energy Pop user, Sunrise City's lead over
non-pop songs shrank from ~2 points to ~1, and Gym Hero (pop) dropped from 2nd to
4th, overtaken by an indie pop and a salsa song with similar energy. Songs with
perfect energy matches (like Bass Overdrive at +2.00) still couldn't reach the top
without genre or mood matches. My conclusion: the change made recommendations
"just different," not more accurate — genre loyalty got diluted and the system
became less confident about what the user actually likes. I reverted to the
original weights afterward.

---

## Limitations and Risks

- **Tiny catalog:** with only 18 songs, one genre match can dominate an entire
  ranking.
- **Genre representation bias:** the "Deep Intense Rock" user only had ONE song
  score above 2.0 (Storm Runner, the only rock track). After that there is a huge
  cliff — the catalog underserves this user, and the system can't say "I don't
  have good options for you."
- **Crowd-pleaser bias:** Gym Hero appears in the top 5 for both the Pop and the
  Rock user because it is pop AND intense AND high-energy — songs that partially
  match everything float to the top of many lists.
- **Exact string matching:** "indie pop" never matches "pop," so related genres
  earn zero genre points. Real systems use similarity, not equality.
- **No lyrics, language, or context:** the system knows nothing about what songs
  mean or when the user is listening.

---

## Reflection

Read and complete `model_card.md`:

[**Model Card**](model_card.md)

(1–2 paragraphs to be written in Phase 5)