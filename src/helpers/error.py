import logging

def error(msg: str) -> str:    
    logging.error(msg)

    response = f"ERROR: \"msg\""
    
    return response 
