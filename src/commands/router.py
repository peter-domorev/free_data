import logging

def router(cmd: str, args: str):
    match message_key:  
        case "ai":
            response = ai_service(message_arguments)
        case "maps":
            response = maps_response()
        case "sms_external":  # text externally
            response = sms_external(message_arguments)
        case "idea":
            response = idea_response(message_arguments)
        case "prank":
            response = prank_response()
        case "helpme": # "help" not available with twillo (unsub)
            response = helpme_response() 
        case "nine11":
            response = nine11_response()
        case "verify":
            response = verify_phone(message_arguments)
        case _:
            response = "No function key recognised"
            logging.warning(f"Unrecognized function key: {message_key}")

            
    print(f"Successfully created response for: {message_key}")
    return response