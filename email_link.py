from simplegmail import Gmail
from simplegmail.query import construct_query

gmail = Gmail()

# For even more control use queries:
# Messages that are: newer than 2 days old, unread, labeled "Finance" or both "Homework" and "CS"
query_params = {
    # "newer_than": (2, "day"),
    # "unread": True,
    # "labels":[["Work"], ["Homework", "CS"]]
}

messages = gmail.get_messages(query=construct_query(query_params))

# Print them out!
for message in messages:
    print("To: " + message.recipient)
    print("From: " + message.sender)
    print("Subject: " + message.subject)
    print("Date: " + message.date)
    print("Preview: " + message.snippet)

    print("Message Body: " + message.plain)
    print(message.attachments)