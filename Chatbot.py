print("🤖 Chatbot: Hello! Type 'bye' to exit.")

while True:
    user = input("You: ").lower()

    if user in ["hi", "hello", "hey"]:
        print("🤖 Chatbot: Hello! How can I help you?")

    elif user in ["how are you"]:
        print("🤖 Chatbot: I'm just a bot, but I'm doing great!")

    elif user in ["what is your name"]:
        print("🤖 Chatbot: I'm your AI chatbot 🤖")

    elif user in ["bye", "exit", "quit"]:
        print("🤖 Chatbot: Goodbye! 👋")
        break

    else:
        print("🤖 Chatbot: Sorry, I don't understand that.")