"""Simple music utilities for code examples."""

CHORDS = {
    "C": ["C", "F", "G"],
    "G": ["G", "C", "D"],
    "F": ["F", "Bb", "C"],
}

def generate_chord_progression(key: str = "C") -> list[str]:
    """Return a basic I-IV-V chord progression for the given key."""
    return CHORDS.get(key.upper(), CHORDS["C"])
