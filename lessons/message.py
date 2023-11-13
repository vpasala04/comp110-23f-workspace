"""Class to store a message (operator overload, union types, default parameters)"""

class Message:

    to: str
    content: str
    important: bool

    def __init__(self, recipient: str, message_content: str, importance_flag: bool):
        """Construct a message."""
        self.to = recipient
        self.content = message_content
        self.important = importance_flag

    def __str__(self) -> str:
        output: str = f"Message to {self.to}:\n"
        output = output + f"Important? {self.important}\n"
        output = output + f'"{self.content}"'
        return output



msg: Message = Message("erin", "Great job!", False)
# msg * 100
print(f"My message is {msg}")
