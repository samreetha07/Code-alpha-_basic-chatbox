def chatbot():
    print("Hi! I'm ChatBox. Type 'bye' to exit.")

    while True:
        user_input = input("You: ").lower()

        if user_input in ['hi', 'hello', 'hey']:
            print("ChatBox: Hello! How can I help you today?")
        elif "your name" in user_input:
            print("ChatBox: I'm ChatBox, your friendly assistant.")
        elif "how are you" in user_input:
            print("ChatBox: I'm just code, but I'm functioning as expected! How about you?")
        elif "weather" in user_input:
            print("ChatBox: I can't fetch live weather, but I hope it's nice outside!")
        elif "bye" in user_input:
            print("ChatBox: Goodbye! Have a great day!")
            break
        else:
            print("ChatBox: I'm sorry, I didn't understand that.")

chatbot()
