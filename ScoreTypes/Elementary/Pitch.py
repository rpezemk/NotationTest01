from NoteName import NoteName

class Pitch:
    def __init__(self, octave: int = 5, noteName: NoteName = NoteName.C, accidental: int = 0):
        self.noteName = noteName
        self.accidental = accidental
        self.octave = octave
    @property
    def total_pitch(self):
        # Calculate the total duration considering both dotting and the base duration
        return 12 * self.octave + self.noteName.pitch + self.accidental 