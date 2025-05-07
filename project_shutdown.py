def shutdown(user_input):
    if user_input.lower() == "yes":
        return "Shutting down..."
    elif user_input.lower() == "no":
        return "Shutdown aborted!"
    else:
        return "Sorry, I didn't understand you."

user_response = input("Do you want to shut down the system? (yes/no): ")
print(shutdown(user_response))
