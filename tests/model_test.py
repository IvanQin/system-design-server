from src.communication.model.message import Message
from src.communication.model.message_body import MessageBody
import unittest

class ModelTest(unittest.TestCase):

    def test_create_message(self):
        message = Message("sender_id","receiver_id", MessageBody.get_default_instance())
        self.assertEqual(message.sender_id, "sender_id")
        self.assertEqual(message.receiver_id, "receiver_id")
        self.assertEqual(message.body.action.name, "DEFAULT")

if __name__ == '__main__':
    unittest.main()
