#contains all the data structure. i.e: a rhythm
#all three outputs should come from the same shared object
from dataclasses import dataclass

@dataclass
class Rhythm:
    title: str
    time_signature: str
    instruments: dict[str, list[str]]