BRAILLE_LABELS= {
    "hh": "⠓⠓",
    "hihat": "⠓⠊⠓⠁⠞",
    "hi-hat": "⠓⠊⠓⠁⠞",
    "sn": "⠎⠝",
    "snare": "⠎⠝⠁⠗⠑",
    "bd": "⠃⠙",
    "kick": "⠅⠊⠉⠅",
    "base drum": "⠃⠁⠎⠑ ⠙⠗⠥⠍",
}

def get_braille_label(label):
    normalized = label.strip().lower()
    return BRAILLE_LABELS.get(normalized, label)