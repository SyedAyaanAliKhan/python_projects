import random

class EmailBot:
    def __init__(self, sender_name="Your Name", sender_email="you@example.com"):
        self.sender_name = sender_name
        self.sender_email = sender_email

    def generate_subject(self, topic):
        subject_templates = [
            f"Regarding {topic}",
            f"Important Update on {topic}",
            f"Follow-Up: {topic}",
            f"Discussion Needed: {topic}",
            f"Exploring Opportunities in {topic}"
        ]
        return random.choice(subject_templates)

    def generate_body(self, topic, recipient_name="Sir/Madam"):
        body_templates = [
            f"Dear {recipient_name},\n\nI hope this message finds you well. "
            f"I wanted to reach out regarding {topic}. I believe this is an important matter, "
            f"and I would appreciate your input.\n\nBest regards,\n{self.sender_name}",

            f"Hello {recipient_name},\n\nI am writing to share some thoughts on {topic}. "
            f"This topic has great potential, and I would love to hear your perspective. "
            f"Please let me know your availability to discuss further.\n\nSincerely,\n{self.sender_name}",

            f"Dear {recipient_name},\n\nThis email is about {topic}. "
            f"I wanted to provide you with an update and get your valuable feedback. "
            f"Looking forward to your response.\n\nWarm regards,\n{self.sender_name}"
        ]
        return random.choice(body_templates)

    def create_email(self, topic, recipient_name="Sir/Madam", recipient_email="recipient@example.com"):
        email = {
            "From": f"{self.sender_name} <{self.sender_email}>",
            "To": f"{recipient_name} <{recipient_email}>",
            "Subject": self.generate_subject(topic),
            "Body": self.generate_body(topic, recipient_name)
        }
        return email


# Example usage
if __name__ == "__main__":
    bot = EmailBot(sender_name="Alice Johnson", sender_email="alice@example.com")
    topic = input("Enter the topic of the email: ")
    email = bot.create_email(topic, recipient_name="Mr. Smith", recipient_email="smith@example.com")

    print("\n--- Generated Email ---")
    print(f"From: {email['From']}")
    print(f"To: {email['To']}")
    print(f"Subject: {email['Subject']}")
    print(f"\n{email['Body']}")
