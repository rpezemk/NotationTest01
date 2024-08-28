from enum import Enum

class NoteDotting(Enum):
    NO_DOT = 1         
    DOTTED = 1.5       
    DOUBLE_DOTTED = 1.75 

    @property
    def description(self):
        if self == NoteDotting.NO_DOT:
            return "No dot (1x duration)"
        elif self == NoteDotting.DOTTED:
            return "Dotted (1.5x duration)"
        elif self == NoteDotting.DOUBLE_DOTTED:
            return "Double-dotted (1.75x duration)"

    @classmethod
    def list_dotting(cls):
        return [dotting.description for dotting in cls]
    
    
