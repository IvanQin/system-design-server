from enum import Enum, auto

class Action(Enum):

    DEFAULT = auto()

    def __str__(self):
     return self.name
