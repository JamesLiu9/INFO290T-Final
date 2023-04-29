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

    def test_post_message(self):
        message_count = len(self.chat_room.messages)
        self.assertEqual(message_count, 4)

    def test_edit_message(self):
        message = self.chat_room.messages[0]
        self.chat_room.edit_message(message, "Hello, everyone! I'm back!")
        self.assertEqual(message.content, "Hello, everyone! I'm back!")

    def test_delete_message(self):
        message = self.chat_room.messages[0]
        self.chat_room.delete_message(message)
        message_count = len(self.chat_room.messages)
        self.assertEqual(message_count, 3)

    def test_search_messages_by_user(self):
        messages = self.chat_room.search_messages_by_user(self.user1)
        self.assertEqual(len(messages), 2)

    def test_search_messages_by_keyword(self):
        messages = self.chat_room.search_messages_by_keyword("How")
        self.assertEqual(len(messages), 2)

    def test_search_messages_by_pattern(self):
        messages = self.chat_room.search_messages_by_pattern(r"\bHi\b")
        self.assertEqual(len(messages), 1)

    def test_private_messages(self):
        private_message = self.chat_room.post_message(self.user1, "This is a private message", recipient=self.user2)
        self.assertIsNotNone(private_message.recipient)
        self.assertEqual(private_message.recipient, self.user2)
        private_messages = self.chat_room.get_private_messages(self.user1, self.user2)
        self.assertEqual(len(private_messages), 1)
    def test_group_message(self):
        user3 = self.chat_room.add_user("Charlie")
        group_message = self.chat_room.post_message(self.user1, "Hello, Bob and Charlie!", recipient=None)
        self.assertIsNone(group_message.recipient)
        messages = self.chat_room.search_messages_by_keyword("Charlie")
        self.assertEqual(len(messages), 1)

if __name__ == '__main__':
    unittest.main()

