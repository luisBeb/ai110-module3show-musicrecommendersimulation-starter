"""
Command line runner for the Music Recommender Simulation.

This file helps you quickly run and test your recommender.

You will implement the functions in recommender.py:
- load_songs
- score_song
- recommend_songs
"""

from src.recommender import load_songs, recommend_songs


def show_recommendations(profile_name: str, user_prefs: dict, songs: list, k: int = 5) -> None:
    """Runs the recommender for one profile and prints a readable report."""
    recommendations = recommend_songs(user_prefs, songs, k=k)

    print(f"\n=== {profile_name} ===")
    print(f"User profile: genre={user_prefs['genre']}, "
          f"mood={user_prefs['mood']}, energy={user_prefs['energy']}")
    print("\nTop recommendations:\n")
    for i, (song, score, explanation) in enumerate(recommendations, start=1):
        print(f"  {i}. {song['title']} — {song['artist']}  (Score: {score:.2f})")
        print(f"     Because: {explanation}")
        print()


def main() -> None:
    songs = load_songs("data/songs.csv")

    profiles = {
        "High-Energy Pop": {"genre": "pop", "mood": "happy", "energy": 0.8},
        "Chill Lofi": {"genre": "lofi", "mood": "chill", "energy": 0.35},
        "Deep Intense Rock": {"genre": "rock", "mood": "intense", "energy": 0.95},
    }

    for name, prefs in profiles.items():
        show_recommendations(name, prefs, songs, k=5)


if __name__ == "__main__":
    main()