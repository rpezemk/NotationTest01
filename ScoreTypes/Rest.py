from ScoreTypes.Elementary.Placeholder import PlaceHolder
from ScoreTypes.Elementary.Duration import NoteDuration
from ScoreTypes.Elementary.Dotting import NoteDotting


class Rest(PlaceHolder):
    def __init__(self, duration: NoteDuration = NoteDuration.QUARTER, dotting: NoteDotting = NoteDotting.NO_DOT):
        super().__init__(duration, dotting)