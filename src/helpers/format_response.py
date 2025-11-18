import logging

def format_response(message_key, response):
    response = f"{message_key}\n\n{response}"
        
    logging.info(f"Formatted reponse: {response}")
    return response
