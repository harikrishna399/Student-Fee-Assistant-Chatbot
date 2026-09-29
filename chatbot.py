import aiml

kernel = aiml.Kernel()
kernel.learn("college_fees.aiml")

print("🎓 Student Fee Chatbot")
print("Type college name or EXIT")

while True:
    user_input = input("\nSearch College: ").upper()

    if user_input == "EXIT":
        print("Goodbye!")
        break

    response = kernel.respond(user_input)
    print("\nResult:")
    print(response)