responses = {
    "hello": "Hello! How can I help you today?",
    "how are you": "I'm just a bot, but thanks for asking!",
    "bye": "Goodbye! Have a nice day."
}

print("Simple Chatbot started. Type 'bye' to exit.")
while True:
    user_input = input("You: ").lower().strip()
    if user_input == "bye":
        print("Bot: Goodbye!")
        break
    reply = responses.get(user_input, "I'm not sure how to respond to that.")
    print("Bot:", reply)