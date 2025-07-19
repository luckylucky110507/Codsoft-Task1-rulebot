
# rule_based_chatbot.py

def chatbot():
    print("🤖 Hello! I'm a simple chatbot. Type 'bye' to exit.\n")
    while True:
        user_input = input("You: ").lower().strip()

        if any(word in user_input for word in ["hello", "hi", "hey"]):
            print("Bot: Hello! How can I assist you today?")
        elif "your name" in user_input:
            print("Bot: I'm RuleBot, your friendly chatbot!")
        elif "how are you" in user_input:
            print("Bot: I'm just code, but I'm running smoothly 😄")
        elif "what can you do" in user_input:
            print("Bot: I can answer simple questions using predefined rules.")
        elif "bye" in user_input:
            print("Bot: Goodbye! Have a great day.")
            break
        else:
            print("Bot: Sorry, I didn't understand that. Can you rephrase?")

if __name__ == "__main__":
    chatbot()
