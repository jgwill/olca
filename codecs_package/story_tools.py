"""Tools for generating simple three-act stories."""

def generate_three_act_story(topic: str = "adventure") -> str:
    """Return a minimal three-act story string."""
    return (
        f"Act I: Our hero begins a {topic}.\n"
        f"Act II: Challenges arise during the {topic}.\n"
        f"Act III: The {topic} concludes with a lesson."
    )
