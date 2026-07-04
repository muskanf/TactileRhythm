# Define a function that creates table data from a Rhythm object.
def make_table(rhythm):
    # Create table headers starting with the instrument column.
    headers = ["Instrument"]

    # Add one numbered column for each position in the rhythm.
    for position in range(1, rhythm.positions + 1):
        # Add the position number as text.
        headers.append(str(position))

    # Create an empty list to store table rows.
    rows = []

    # Loop through each instrument and its rhythm pattern.
    for instrument_name, pattern in rhythm.instruments.items():
        # Start each row with the instrument name.
        row = [instrument_name]

        # Add the instrument's rhythm symbols after the instrument name.
        row.extend(pattern)

        # Add the completed row to the list of rows.
        rows.append(row)

    # Return all table information as a dictionary.
    return {
        "headers": headers,
        "rows": rows,
    }