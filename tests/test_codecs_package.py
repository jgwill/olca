from codecs_package import generate_chord_progression, generate_three_act_story


def test_generate_chord_progression():
    chords = generate_chord_progression("C")
    assert chords == ["C", "F", "G"]


def test_generate_three_act_story():
    story = generate_three_act_story("journey")
    assert "Act I" in story and "journey" in story
