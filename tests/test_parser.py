# Import the parser function we want to test.
from tactile_rhythm.parser import parse_rhythm
# Define a test for the basic rock example.
def test_parse_basic_rock():
    # Create a sample rhythm input.
    text = """title: Basic Rock Beat
time: 4/4

hihat: x x x x x x x x
snare: . . x . . . x .
kick:  x . . . x . . ."""

    # Parse the sample input.
    rhythm = parse_rhythm(text)

    # Check that the title was parsed correctly.
    assert rhythm.title == "Basic Rock Beat"

    # Check that the time signature was parsed correctly.
    assert rhythm.time_signature == "4/4"

    # Check that the number of positions was parsed correctly.
    assert rhythm.positions == 8

    # Check that the kick pattern was parsed correctly.
    assert rhythm.instruments["kick"] == ["x", ".", ".", ".", "x", ".", ".", "."]

    # Check that the snare pattern was parsed correctly.
    assert rhythm.instruments["snare"] == [".", ".", "x", ".", ".", ".", "x", "."]

    # Check that the hihat pattern was parsed correctly.
    assert rhythm.instruments["hihat"] == ["x", "x", "x", "x", "x", "x", "x", "x"]


# Define a test for invalid symbols.
def test_invalid_symbol_raises_error():
    # Create input with an invalid symbol.
    text = """title: Bad Rhythm
time: 4/4

kick: x o . ."""

    # Try to parse the bad input and expect an error.
    try:
        # Parse the invalid input.
        parse_rhythm(text)

        # Fail the test if no error happens.
        assert False

    # Catch the expected ValueError.
    except ValueError as error:
        # Check that the error message mentions the invalid symbol.
        assert "Invalid symbol" in str(error)


# Define a test for uneven row lengths.
def test_uneven_lengths_raise_error():
    # Create input where rows have different lengths.
    text = """title: Uneven Rhythm
time: 4/4

kick: x . x .
snare: . x ."""

    # Try to parse the uneven input and expect an error.
    try:
        # Parse the invalid input.
        parse_rhythm(text)

        # Fail the test if no error happens.
        assert False

    # Catch the expected ValueError.
    except ValueError as error:
        # Check that the error message mentions the mismatch.
        assert "expects" in str(error)