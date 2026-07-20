# Note: Using dictionary + .get() instead of if-elif chains,
# as recommended in the "Hash Maps & Dictionaries" section 
# of the Project 1 brief for better scalability.

print("Bot: Hi! I'm a simple chatbot.")
print("Bot: Try saying one of these:")
print("- hello")
print("- how are you")
print("- thanks")
print("- help")
print("- bye (to exit)")

responses = {
    "hello": "Hi there!",
    "how are you": "I am doing great!",
    "help": "I can chat about simple things!",
    "thanks": "You are welcome!",
    "bye": "Goodbye!"
    
}

while True:
    user_input = input("You: ")
    clean_input =user_input.lower().strip()
    
    if clean_input == "bye" or clean_input == "exit":
        print("Bot: Goodbye!")
        break
    
    reply = responses.get(clean_input, "I dont understand that")
    print("Bot:", reply)