import unittest
from chat_room import ChatRoom, User


class TestChatRoom(unittest.TestCase):
    def setUp(self):
        self.chat_room = ChatRoom()
        self.user1 = self.chat_room.add_user("Alice")
        self.user2 = self.chat_room.add_user("Bob")
        self.chat_room.post_message(self.user1, "Hello, everyone!")
        self.chat_room.post_message(self.user2, "Hi, Alice!")
        self.chat_room.post_message(self.user1, "How are you, Bob?")
        self.chat_room.post_message(self.user2, "I'm doing great! How about you?")

if __name__ == '__main__':
    unittest.main()

