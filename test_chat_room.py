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

    def test_add_and_remove_user(self):
        user_count = len(self.chat_room.users)
        self.assertEqual(user_count, 2)
        user3 = self.chat_room.add_user("Charlie")
        user_count = len(self.chat_room.users)
        self.assertEqual(user_count, 3)
        self.chat_room.remove_user(user3)
        user_count = len(self.chat_room.users)
        self.assertEqual(user_count, 2)

    # Add other tests here with the same indentation as the first test

if __name__ == '__main__':
    unittest.main()

