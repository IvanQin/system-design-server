from .message_action import Action

class MessageBody():
    def __init__(self, action : Action):
        self.action = action

    @staticmethod
    def get_default_instance() :
        return MessageBody(Action.DEFAULT)

    def __str__(self):
        return f'{str(self.action)}'
