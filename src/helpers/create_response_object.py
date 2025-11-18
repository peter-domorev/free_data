import logging
from twilio.twiml.messaging_response import MessagingResponse

def create_response_object(response):
    response_object = MessagingResponse().message()
    logging.info(f"Sending message: {response}")
    return str(response_object)