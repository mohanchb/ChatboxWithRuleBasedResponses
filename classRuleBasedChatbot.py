class RuleBasedChatbot:
    def __init__(self):
        self.rules = {
            "hello": "Hello! Hello",
            "how are you": "I'm just a chatbot, but I'm here to help!",
            "bye": "Goodbye! Have a great day!",
        }

    def get_response(self, user_input):
        user_input = user_input.lower()
        for keyword in self.rules:
            if keyword in user_input:
                return self.rules[keyword]
        return "I'm sorry, I don't understand that."

# Create an instance of the chatbot
chatbot = RuleBasedChatbot()

# Start a conversation
print("Rule-Based Chatbot: Hello! How can I assist you?")
while True:
    user_input = input("You: ")
    if user_input.lower() == "exit":
        print("Rule-Based Chatbot: Goodbye!")
        break
    response = chatbot.get_response(user_input)
    print("Rule-Based Chatbot:", response)
