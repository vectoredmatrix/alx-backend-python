# new.py
import os
import django

# Setup Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "messaging_app.settings")
django.setup()

from chats.models import User, Conversation, Message

# 1. Clear old data
Message.objects.all().delete()
Conversation.objects.all().delete()
User.objects.all().delete()
# new.py
import os
import django
import random

# Setup Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "messaging_app.settings")
django.setup()

from chats.models import User, Conversation, Message

# 1. Clear old data
Message.objects.all().delete()
Conversation.objects.all().delete()
User.objects.all().delete()

# 2. Create Users
users = [
    User.objects.create_user(username="alice", password="pass123", role="GUEST"),
    User.objects.create_user(username="bob", password="pass123", role="HOST"),
    User.objects.create_user(username="charlie", password="pass123", role="GUEST"),
    User.objects.create_user(username="david", password="pass123", role="GUEST"),
    User.objects.create_user(username="eve", password="pass123", role="HOST"),
    User.objects.create_user(username="frank", password="pass123", role="ADMIN"),
]

# Unpack for convenience
alice, bob, charlie, david, eve, frank = users

# 3. Create Conversations
c1 = Conversation.objects.create()  # Alice + Bob (private chat)
c2 = Conversation.objects.create()  # Alice + Charlie (private chat)
c3 = Conversation.objects.create()  # Group chat: Alice, Bob, Charlie
c4 = Conversation.objects.create()  # Group chat: David, Eve, Frank

# 4. Add participants
c1.participants_id.set([alice, bob])
c2.participants_id.set([alice, charlie])
c3.participants_id.set([alice, bob, charlie])   # group chat
c4.participants_id.set([david, eve, frank])     # group chat

# 5. Create Messages
# Private chat Alice <-> Bob
Message.objects.create(sender_id=alice, conversation=c1, message_body="Hello Bob!")
Message.objects.create(sender_id=bob, conversation=c1, message_body="Hi Alice!")
Message.objects.create(sender_id=alice, conversation=c1, message_body="How are you?")

# Private chat Alice <-> Charlie
Message.objects.create(sender_id=alice, conversation=c2, message_body="Hey Charlie!")
Message.objects.create(sender_id=charlie, conversation=c2, message_body="Yo Alice!")
Message.objects.create(sender_id=alice, conversation=c2, message_body="Long time no see.")

# Group chat Alice, Bob, Charlie
Message.objects.create(sender_id=alice, conversation=c3, message_body="Hey team!")
Message.objects.create(sender_id=bob, conversation=c3, message_body="Hi all.")
Message.objects.create(sender_id=charlie, conversation=c3, message_body="What’s up guys?")

# Group chat David, Eve, Frank
Message.objects.create(sender_id=david, conversation=c4, message_body="Hello group!")
Message.objects.create(sender_id=eve, conversation=c4, message_body="Hi David & Frank.")
Message.objects.create(sender_id=frank, conversation=c4, message_body="Welcome guys!")

# Extra: Random chatter in c3 (group chat)
for i in range(5):
    sender = random.choice([alice, bob, charlie])
    Message.objects.create(
        sender_id=sender,
        conversation=c3,
        message_body=f"Random msg {i+1} from {sender.username}"
    )

print("✅ Database repopulated with users, private chats, and group chats.")

# 2. Create Users
u1, _ = User.objects.get_or_create(username="alice", defaults={"password": "pass123", "role": "GUEST"})
u2, _ = User.objects.get_or_create(username="bob", defaults={"password": "pass123", "role": "HOST"})
u3, _ = User.objects.get_or_create(username="charlie", defaults={"password": "pass123", "role": "GUEST"})

# 3. Create Conversations
c1 = Conversation.objects.create()
c2 = Conversation.objects.create()

# 4. Add participants
c1.participants_id.set([u1, u2])       # Alice + Bob
c2.participants_id.set([u1, u3])       # Alice + Charlie

# 5. Create Messages
Message.objects.create(sender_id=u1, conversation=c1, message_body="Hello Bob!")
Message.objects.create(sender_id=u2, conversation=c1, message_body="Hi Alice!")
Message.objects.create(sender_id=u1, conversation=c2, message_body="Hey Charlie!")
Message.objects.create(sender_id=u3, conversation=c2, message_body="Yo Alice!")

print("✅ Database repopulated with test data.")
