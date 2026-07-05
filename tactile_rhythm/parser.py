#This file turns user text into a rhythm object.
# Import the Rhythm data model.
from tactile_rhythm.models import Rhythm
# Define the main parser function.
def parse_rhythm(text: str) -> Rhythm:
    # Check whether the user entered empty text.
    if not text.strip():
        # Raise error if the input is empty.
        raise ValueError("Please enter a rhythm specification.")

    # Split the input text into individual lines.
    raw_lines = text.splitlines()

    # Remove blank lines and strip spaces from each line.
    lines = [line.strip() for line in raw_lines if line.strip()]

    # Create a default title in case the user does not provide one.
    title = "Untitled Rhythm"

    # Create a default time signature in case the user does not provide one.
    time_signature = "4/4"

    # Create an empty dictionary for instruments.
    instruments = {}
    # Loop through each cleaned line.
    for line in lines:
        # Check that the line contains a colon.
        if ":" not in line:
            # Raise an error for invalid lines.
            raise ValueError(f"Invalid line: '{line}'. Each line should contain a colon.")

        # Split the line into a left side and right side at the first colon.
        key, value = line.split(":", 1)

        # Normalize the key by stripping spaces and making it lowercase.
        key = key.strip().lower()

        # Strip extra spaces from the value.
        value = value.strip()

        # Check whether this line defines the title.
        if key == "title":
            # Store the title.
            title = value
            # Move to the next line.
            continue

        # Check whether this line defines the time signature.
        if key == "time":
            # Store the time signature.
            time_signature = value

            # Move to the next line.
            continue

        # Treat every other key as an instrument name.
        instrument_name = key

        # Split the instrument pattern into symbols.
        pattern = value.split()

        # Check that the pattern is not empty.
        if not pattern:
            # Raise an error if an instrument has no rhythm symbols.
            raise ValueError(f"The instrument '{instrument_name}' has no rhythm pattern.")

        # Check that every symbol is allowed.
        for symbol in pattern:
            # Allow x for a played note and . for a rest.
            if symbol not in ["x", "."]:
                # Raise an error if the symbol is unknown.
                raise ValueError(
                    f"Invalid symbol '{symbol}' in '{instrument_name}'. Use only 'x' and '.'."
                )

        # Store the instrument pattern.
        instruments[instrument_name] = pattern

    # Check that at least one instrument was provided.
    if not instruments:
        # Raise an error if the input only has title/time and no rhythm rows.
        raise ValueError("Please include at least one instrument pattern, such as 'kick: x . x .'.")

    # Get the length of the first instrument pattern.
    positions = len(next(iter(instruments.values())))

    # Check that all instruments have the same number of positions.
    for instrument_name, pattern in instruments.items():
        # Compare this pattern length with the expected length.
        if len(pattern) != positions:
            # Raise an error if one row is shorter or longer than the others.
            raise ValueError(
                f"The instrument '{instrument_name}' has {len(pattern)} positions, "
                f"but the rhythm expects {positions} positions."
            )

    # Return the final structured Rhythm object.
    return Rhythm(
        title=title,
        time_signature=time_signature,
        instruments=instruments,
        positions=positions,
    )