from enum import Enum

class NoteName(Enum):
    C = 0
    D = 2
    E = 4
    F = 5
    G = 7
    A = 9
    B = 11

    @property
    def pitch(self):
        return self.value

    @staticmethod
    def from_pitch(pitch):
        for note in NoteName:
            if note.value == pitch:
                return note
        raise ValueError(f"No note found for pitch {pitch}")



# if __name__ == "__main__":
#     # Example usage:
#     for note in NoteName:
#         print(f"{note.name}: {note.pitch}")

#     # Convert pitch to note
#     try:
#         pitch = 4
#         note = NoteName.from_pitch(pitch)
#         print(f"Pitch {pitch} corresponds to note: {note.name}")
#     except ValueError as e:
#         print(e)
