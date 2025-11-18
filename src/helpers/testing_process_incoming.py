def testing_process_incoming():
    incoming_message = input("TESTING_MODE: Incoming message: ")
    message_key = incoming_message.partition(" ")[0]
    message_arguments = incoming_message.partition(" ")[2]

    return [message_key, message_arguments]
