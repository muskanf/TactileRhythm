#This file generates the tactile-style SVG graphic
# Import html so we can safely escape text inside SVG.
import html
# Define a function that creates an SVG tactile-style graphic.
def make_svg(rhythm):
    # Set the left margin for instrument labels.
    left_margin = 110
    # Set the top margin for the title and headers.
    top_margin = 70
    # Set the horizontal spacing between rhythm positions.
    column_spacing = 55
    # Set the vertical spacing between instrument rows.
    row_spacing = 55
    # Set the radius of played-note markers.
    marker_radius = 11
    # Set the width of the SVG based on the number of rhythm positions.
    width = left_margin + rhythm.positions * column_spacing + 50
    # Set the height of the SVG based on the number of instruments.
    height = top_margin + len(rhythm.instruments) * row_spacing + 50
    # Create a list to store SVG lines.
    svg_parts = []

    # Add the opening SVG tag.
    svg_parts.append(
        f'<svg width="{width}" height="{height}" '
        f'viewBox="0 0 {width} {height}" '
        f'xmlns="http://www.w3.org/2000/svg" '
        f'role="img" '
        f'aria-labelledby="svg-title svg-desc">'
    )

    # Add a title element for screen readers.
    svg_parts.append(f'<title id="svg-title">{html.escape(rhythm.title)} tactile rhythm preview</title>')

    # Add a description element for screen readers.
    svg_parts.append(
        f'<desc id="svg-desc">A tactile-style grid showing {len(rhythm.instruments)} instruments '
        f'across {rhythm.positions} rhythm positions.</desc>'
    )

    # Add a white background.
    svg_parts.append(f'<rect width="{width}" height="{height}" fill="white" />')

    # Add the rhythm title as visible text.
    svg_parts.append(
        f'<text x="20" y="30" font-size="22" font-family="Arial" font-weight="bold">'
        f'{html.escape(rhythm.title)}</text>'
    )

    # Add the time signature as visible text.
    svg_parts.append(
        f'<text x="20" y="55" font-size="16" font-family="Arial">'
        f'Time: {html.escape(rhythm.time_signature)}</text>'
    )

    # Add column position labels.
    for position in range(1, rhythm.positions + 1):
        # Calculate the x coordinate for this position.
        x = left_margin + (position - 1) * column_spacing

        # Add the position number above the grid.
        svg_parts.append(
            f'<text x="{x}" y="{top_margin - 15}" text-anchor="middle" '
            f'font-size="14" font-family="Arial">{position}</text>'
        )

    # Loop through each instrument row.
    for row_index, (instrument_name, pattern) in enumerate(rhythm.instruments.items()):
        # Calculate the y coordinate for this row.
        y = top_margin + row_index * row_spacing

        # Add the instrument label on the left.
        svg_parts.append(
            f'<text x="20" y="{y + 5}" font-size="16" font-family="Arial">'
            f'{html.escape(instrument_name)}</text>'
        )

        # Draw a horizontal guide line for the instrument row.
        svg_parts.append(
            f'<line x1="{left_margin - 25}" y1="{y}" '
            f'x2="{width - 35}" y2="{y}" '
            f'stroke="black" stroke-width="2" />'
        )

        # Loop through each rhythm symbol in the row.
        for position_index, symbol in enumerate(pattern):
            # Calculate the x coordinate for this rhythm position.
            x = left_margin + position_index * column_spacing

            # Draw a small vertical tick mark at each position.
            svg_parts.append(
                f'<line x1="{x}" y1="{y - 10}" '
                f'x2="{x}" y2="{y + 10}" '
                f'stroke="black" stroke-width="1" />'
            )

            # Check whether the instrument plays at this position.
            if symbol == "x":
                # Draw a filled circle for a played note.
                svg_parts.append(
                    f'<circle cx="{x}" cy="{y}" r="{marker_radius}" '
                    f'fill="black" stroke="black" stroke-width="2" />'
                )

            # Check whether the instrument rests at this position.
            else:
                # Draw a small open circle for a rest.
                svg_parts.append(
                    f'<circle cx="{x}" cy="{y}" r="4" '
                    f'fill="white" stroke="black" stroke-width="1" />'
                )

    # Add the closing SVG tag.
    svg_parts.append("</svg>")

    # Join all SVG lines into one string.
    return "\n".join(svg_parts)