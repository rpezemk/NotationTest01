from ScoreTypes.Elementary.Duration import NoteDuration
from ScoreTypes.Elementary.Dotting import NoteDotting

class PlaceHolder:
    def __init__(self, duration: NoteDuration = NoteDuration.QUARTER, dotting: NoteDotting = NoteDotting.NO_DOT):
        self.duration = duration
        self.dotting = dotting
        
        
    @property
    def total_duration(self):
        # Calculate the total duration considering both dotting and the base duration
        return self.duration.value * self.dotting.value

    def __str__(self):
        return f"Duration: {self.duration.name.replace('_', ' ')} ({self.duration.value}), " \
               f"Dotting: {self.dotting.name.replace('_', ' ')} ({self.dotting.value}), " \
               f"Total Duration: {self.total_duration}"

