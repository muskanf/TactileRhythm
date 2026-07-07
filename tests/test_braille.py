from tactile_rhythm.braille import get_braille_label

def test_known_braille_label():
    assert get_braille_label("SN") == "⠎⠝"

def test_unknown_label_returns_original():
    assert get_braille_label("cowbell") == "cowbell"