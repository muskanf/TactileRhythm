from tactile_rhythm.parser import parse_rhythm

def test_parse_basic_rock():
    text = """
title: Basic Rock Beat
time: 4/4

hihat: x x x x x x x x
snare: . . x . . . x .
kick:  x . . . x . . .
"""
    rhythm = parse_rhythm(text)

    assert rhythm.title == "Basic Rock Beat"
    assert rhythm.time_signature == "4/4"
    assert rhythm.instruments["kick"] == ["x", ".", ".", ".", "x", ".", ".", "."]