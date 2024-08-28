from ScoreTypes.Elementary.Duration import NoteDuration
from ScoreTypes.Elementary.Dotting import NoteDotting
from ScoreTypes.Elementary.Pitch import Pitch
from ScoreTypes.Elementary.Placeholder import PlaceHolder

class Note:
    def __init__(self, pitch: Pitch = Pitch(), placeholder: PlaceHolder = PlaceHolder()):
        self.pitch = pitch
        self.placeholder = placeholder