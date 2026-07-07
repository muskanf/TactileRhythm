
## `app.py`
# Import Flask so we can create a small web application.
from flask import Flask, render_template, request
# Import the parser function that converts text input into a Rhythm object.
from tactile_rhythm.parser import parse_rhythm
# Import the table renderer that converts a Rhythm object into table data.
from tactile_rhythm.render_table import make_table
# Import the navigation renderer that converts a Rhythm object into text/list data.
from tactile_rhythm.render_navigation import make_navigation
# Import the SVG renderer that converts a Rhythm object into a tactile-style SVG string.
from tactile_rhythm.render_svg import make_svg
from tactile_rhythm.braille import get_braille_label
# Create the Flask application.
app = Flask(__name__)
# Define the homepage route.
@app.route("/", methods=["GET"])
def index():
    # Create example text that will appear in the textarea by default.
    example_text = """title: Basic Rock Beat
time: 4/4

hihat: x x x x x x x x
snare: . . x . . . x .
kick:  x . . . x . . ."""

    # Rendering the homepage template and pass in the example rhythm text.
    return render_template("index.html", example_text=example_text)


# Define the compile route that receives rhythm text from the form.
@app.route("/compile", methods=["POST"])
def compile_rhythm():
    # Get the submitted rhythm text from the form.
    rhythm_text = request.form.get("rhythm_text", "")

    # Check whether the braille checkbox was selected.
    show_braille = request.form.get("show_braille") == "yes"

    # Try to parse and render the rhythm.
    try:
        # Convert the user's text into a structured Rhythm object.
        rhythm = parse_rhythm(rhythm_text)

        # Create an empty braille legend.
        braille_legend = []

        # Only create the braille legend if the checkbox was selected.
        if show_braille:
            # Loop through the instrument names in the parsed rhythm.
            for instrument_name in rhythm.instruments.keys():
                # Add the print label and braille label to the legend.
                braille_legend.append({
                    "label": instrument_name,
                    "braille": get_braille_label(instrument_name)
                })

        # Convert the Rhythm object into table data.
        table = make_table(rhythm)

        # Convert the Rhythm object into a navigable position-by-position list.
        navigation = make_navigation(rhythm)

        # Convert the Rhythm object into an SVG tactile-style preview.
        svg = make_svg(rhythm, show_braille=show_braille)

        # Render the results page with all generated outputs.
        return render_template(
            "result.html",
            rhythm=rhythm,
            rhythm_text=rhythm_text,
            table=table,
            navigation=navigation,
            svg=svg,
            error=None,
            show_braille=show_braille,
            braille_legend=braille_legend,
        )

    # Catch any parsing/rendering error so the app does not crash.
    except ValueError as error:
        # Render the homepage again and show the error message.
        return render_template(
            "index.html",
            example_text=rhythm_text,
            error=str(error),
        )


if __name__ == "__main__":
    app.run(debug=True)