from enum import Enum, auto

class Action(Enum):

    DEFAULT = auto()
    INCREMENT_VALUE = auto()
    DECREMENT_VALUE = auto()
    HEARTBEAT = auto()

    def __str__(self):
     return self.name
