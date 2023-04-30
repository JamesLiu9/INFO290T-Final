import re
from datetime import datetime

class User:
    def __init__(self, username):
        self.username = username

class Message:
    def __init__(self, user, content, timestamp=None, recipient=None):
        self.user = user
        self.content = content
        self.timestamp = timestamp or datetime.now()
        self.recipient = recipient

class ChatRoom:
    def __init__(self):
        self.users = set()
        self.messages = []

    def add_user(self, username):
        user = User(username)
        self.users.add(user)
        return user

    def remove_user(self, user):
        self.users.discard(user)

    def post_message(self, user, content, recipient=None):
        if user not in self.users:
            return None
        message = Message(user, content, recipient=recipient)
        self.messages.append(message)
        return message

    def edit_message(self, message, new_content):
        if message in self.messages:
            message.content = new_content

    def delete_message(self, message):
        if message in self.messages:
            self.messages.remove(message)

    def search_messages_by_user(self, user):
        return [msg for msg in self.messages if msg.user == user]

    def search_messages_by_keyword(self, keyword):
        return [msg for msg in self.messages if keyword.lower() in msg.content.lower()]

    def search_messages_by_pattern(self, pattern):
        regex = re.compile(pattern, re.IGNORECASE)
        return [msg for msg in self.messages if regex.search(msg.content)]

    def get_private_messages(self, user1, user2):
        return [msg for msg in self.messages if (msg.user == user1 and msg.recipient == user2) or (msg.user == user2 and msg.recipient == user1)]

    def get_messages_in_date_range(self, start_date, end_date):
        messages_in_range = []
        for message in self.messages:
            if start_date <= message.timestamp <= end_date:
                messages_in_range.append(message)
        return messages_in_range