# Define a helper function to format a list of instruments as readable text.
def format_instrument_list(instruments):
    # If no instruments are playing, return "rest".
    if not instruments:
        return "rest"

    # If one instrument is playing, return only that instrument.
    if len(instruments) == 1:
        return instruments[0]

    # If two instruments are playing, join them with "and".
    if len(instruments) == 2:
        return f"{instruments[0]} and {instruments[1]}"

    # If three or more instruments are playing, use commas and "and".
    return f"{', '.join(instruments[:-1])}, and {instruments[-1]}"


# Define a function that creates a navigable text representation.
def make_navigation(rhythm):
    # Create an empty list to store navigation items.
    navigation_items = []

    # Loop through each position in the rhythm.
    for position_index in range(rhythm.positions):
        # Create an empty list for instruments playing at this position.
        playing = []

        # Loop through each instrument and its pattern.
        for instrument_name, pattern in rhythm.instruments.items():
            # Check whether the current instrument plays at this position.
            if pattern[position_index] == "x":
                playing.append(instrument_name)

        # Convert the playing instruments into a readable phrase.
        playing_text = format_instrument_list(playing)

        # Create a sentence for this position.
        sentence = f"Position {position_index + 1}: {playing_text}."

        # Add the sentence to the navigation list.
        navigation_items.append(sentence)

    # Return the final list of navigation sentences.
    return navigation_items