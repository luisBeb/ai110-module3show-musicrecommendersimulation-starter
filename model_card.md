# 🎧 Model Card: Music Recommender Simulation

## 1. Model Name

**VibraFinder 1.0**

---

## 2. Intended Use

VibraFinder generates ranked, explained song recommendations from a small catalog
based on a user's taste profile (favorite genre, favorite mood, and target energy
level). It assumes the user can describe their taste with those three values and
that their taste is consistent (one genre, one mood). It is built for classroom
exploration of how recommender systems work — it is not intended for real users or
production use.

---

## 3. How the Model Works

Each song in the catalog is judged against the user's taste profile, like a judge
giving points in a contest. A song earns 2 points if its genre matches the user's
favorite genre, 1 point if its mood matches, and up to 1 extra point depending on
how close its energy level is to the user's target — the closer, the more points.
Genre is worth double because it is usually the strongest signal of what someone
likes. Every song gets a total score plus a list of the reasons it earned points,
then the whole catalog is sorted and the top 5 are recommended. I started from
starter code with empty functions and implemented the loading, scoring, and
ranking logic myself following this recipe.

---

## 4. Data

The catalog is a CSV with 18 songs. I started with 10 starter songs (pop, lofi,
rock, ambient, jazz, synthwave, indie pop) and added 8 more covering genres and
moods that were missing: reggaeton, salsa, EDM, metal, R&B, trap, bachata, and
classical, with new moods like party, romantic, and calm. Each song has genre,
mood, energy, tempo, valence, danceability, and acousticness — though my scoring
only uses genre, mood, and energy. Big parts of musical taste are still missing:
lyrics, language, artist popularity, era, and personal history with a song. Most
genres have only one representative track, so coverage is very thin.

---

## 5. Strengths

- For well-represented tastes the results feel right: the Chill Lofi profile got
  all three lofi songs ranked in the top 3, and the system correctly ranked
  "focused" lofi below "chill" lofi by withholding the mood point.
- Library Rain scored a perfect 4.00 for the Chill Lofi user (exact genre, mood,
  and energy match), which matches intuition exactly.
- Every recommendation comes with human-readable reasons ("genre match (+2.0)"),
  so the ranking is never a black box.

---

## 6. Limitations and Bias

- **Underrepresentation cliff:** the Deep Intense Rock user got only ONE song
  above 2.0 points (Storm Runner, the only rock track), then a huge drop. The
  system cannot signal "I have nothing good for you" — it just fills slots with
  weak matches.
- **Crowd-pleaser bias:** Gym Hero (pop + intense + high energy) appears in the
  top 5 for both the Pop user and the Rock user, because songs that partially
  match everything float to the top of many lists.
- **Exact string matching:** "indie pop" earns zero genre points for a "pop"
  user even though the genres are clearly related.
- **Unused features:** tempo, valence, danceability, and acousticness exist in
  the data but never affect the score, so two songs identical in genre/mood/energy
  are indistinguishable.
- **Single-taste assumption:** users who like multiple genres or shifting moods
  can't be represented by one profile.

---

## 7. Evaluation

I tested three deliberately different profiles: High-Energy Pop (pop/happy/0.8),
Chill Lofi (lofi/chill/0.35), and Deep Intense Rock (rock/intense/0.95), running
the recommender for each and pasting the terminal outputs below. I checked whether
the top results matched intuition, whether any song appeared across all profiles,
and how big the score gaps were. I also ran a Weight Shift experiment (genre
halved, energy doubled): the top picks barely changed but score gaps compressed —
a pop lover saw salsa and indie pop rated almost as high as real pop. The change
made results "just different," not more accurate, so I reverted it. What surprised
me most was the rock user's cliff: I expected the catalog to serve all profiles
roughly equally, but representation in the data mattered more than the scoring
logic.

**Profile comparisons:**

- **Pop vs. Lofi:** the outputs share zero songs — high-energy happy tracks
  versus low-energy chill tracks. This makes sense: the profiles differ on all
  three features, so the rankings flipped almost completely.
- **Pop vs. Rock:** both top-5 lists include Gym Hero, but for different reasons
  (genre match for the pop user, mood + energy for the rock user). The overlap
  shows how a song that partially matches everything reaches many audiences.
- **Lofi vs. Rock:** the lofi user's list is dominated by genre matches (three
  lofi tracks), while the rock user's list is mostly energy-only matches after
  Storm Runner — evidence that the catalog serves one taste much better than the
  other.

### Sample outputs

```
=== High-Energy Pop ===
User profile: genre=pop, mood=happy, energy=0.8

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

=== Chill Lofi ===
User profile: genre=lofi, mood=chill, energy=0.35

  1. Library Rain — Paper Lanterns  (Score: 4.00)
     Because: genre match (+2.0), mood match (+1.0), energy similarity (+1.00)
  2. Midnight Coding — LoRoom  (Score: 3.93)
     Because: genre match (+2.0), mood match (+1.0), energy similarity (+0.93)
  3. Focus Flow — LoRoom  (Score: 2.95)
     Because: genre match (+2.0), energy similarity (+0.95)
  4. Spacewalk Thoughts — Orbit Bloom  (Score: 1.93)
     Because: mood match (+1.0), energy similarity (+0.93)
  5. Coffee Shop Stories — Slow Stereo  (Score: 0.98)
     Because: energy similarity (+0.98)

=== Deep Intense Rock ===
User profile: genre=rock, mood=intense, energy=0.95

  1. Storm Runner — Voltline  (Score: 3.96)
     Because: genre match (+2.0), mood match (+1.0), energy similarity (+0.96)
  2. Gym Hero — Max Pulse  (Score: 1.98)
     Because: mood match (+1.0), energy similarity (+0.98)
  3. Iron Tempest — Graveshade  (Score: 1.98)
     Because: mood match (+1.0), energy similarity (+0.98)
  4. Bass Overdrive — Kilowatt Kids  (Score: 1.00)
     Because: energy similarity (+1.00)
  5. Calle Caliente — Ritmo Nuevo  (Score: 0.93)
     Because: energy similarity (+0.93)
```

---

## 8. Future Work

- Use partial genre similarity (e.g., "indie pop" earns half credit for "pop")
  instead of exact string matching.
- Incorporate the unused features (valence, danceability, acousticness) — for
  example, use `likes_acoustic` from the UserProfile to reward acoustic tracks.
- Add a diversity rule so the top 5 doesn't come from one genre.
- Support multiple favorite genres/moods per user.
- Show a confidence warning when the catalog has few good matches (the "rock
  cliff" problem).

---

## 9. Personal Reflection

My biggest learning moment was seeing how much the *data* matters compared to the
*algorithm*. My scoring logic treated every user identically, but the rock user
still got much worse recommendations than the lofi user simply because the catalog
only had one rock song. Bias didn't come from bad code — it came from what was and
wasn't in the CSV. Using AI tools helped me implement and iterate quickly, but I
had to verify things myself, like running the recommender before and after the
weight experiment to check my expectations against real output (my predictions
were partly wrong — rankings changed less than I expected). It surprised me how
much a system this simple — three if-statements and a sort — already "feels" like
a real recommender once it explains its reasons. It changed how I look at Spotify:
when it recommends something weird, I now wonder whether that's the algorithm or
just gaps in what it knows about me.