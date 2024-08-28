from enum import Enum

class NoteDuration(Enum):
    SIXTY_FOURTH = 1 / 64
    THIRTY_SECOND = 1 / 32
    SIXTEENTH = 1 / 16
    EIGHTH = 1 / 8
    QUARTER = 1 / 4
    HALF = 1 / 2
    WHOLE = 1
    BREVE = 2  # Twice the length of a whole note
    LONGA = 4  # Four times the length of a whole note

    @property
    def name_with_duration(self):
        if self.value == int(self.value):  # For whole and longer notes
            return f"{self.name.replace('_', ' ')} (x{int(self.value)})"
        else:
            return f"{self.name.replace('_', ' ')} (1/{int(1 / self.value)})"

    @classmethod
    def list_durations(cls):
        return [duration.name_with_duration for duration in cls]