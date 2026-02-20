responses = { 
    # paste your full responses dictionary here
}

def get_response(user_input):
    user_input = user_input.lower().strip()

    if user_input in responses:
        return responses[user_input]
    else:
        return "Sorry, I don't know that yet."