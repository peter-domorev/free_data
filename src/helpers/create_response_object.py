import logging
from twilio.twiml.messaging_response import MessagingResponse

def create_response_object(response):
    response_object = str(MessagingResponse().message())
    logging.info(f"Created response object: {response_object}")
    return str(response_object)