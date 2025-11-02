def chatbot_response(user_input):
    """Return a chatbot response based on user input."""
    user_input = user_input.lower()

    if "hello" in user_input or "hi" in user_input:
        return "Hi there! How can I help you today?"
    elif "how are you" in user_input:
        return "I'm just a bunch of Python code, but I'm doing great!"
    elif "your name" in user_input:
        return "I'm ChatBuddy, your friendly Python chatbot"
    elif "thank" in user_input:
        return "You're welcome!"
    elif "help" in user_input:
        return "I can respond to greetings, tell my name, and say goodbye. Try saying 'hello' or 'how are you'."
    else:
        return "I'm not sure how to respond to that. Try something else!"

# -----------------------------------------------------------

print("💬 Welcome to ChatBuddy — your basic Python chatbot!")
print("Type 'bye' anytime to end the chat.\n")

while True:
    user_message = input("You: ")

    # exit condition
    if "bye" in user_message.lower():
        print("ChatBuddy: Goodbye! It was nice chatting with you.")
        break

    response = chatbot_response(user_message)
    print(f"ChatBuddy: {response}")
