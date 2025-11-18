import ollama
#from annotated_types.test_cases import cases
from twilio.rest import Client
from flask import Flask, request
import subprocess
import re
import logging

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(funcName)s: %(message)s"
)

TESTING_MODE = True

if not TESTING_MODE:
    app = Flask(__name__)
    
    @app.route("/sms", methods=["POST"])
    def sms_reply():
        message = process_incoming()
        message_key = message[0]
        message_arguments = message[1]
        
        response = retrieve_response(message_key, message_arguments)           
        return process_outgoing(response)
    
    incoming_message = request.form.get('Body', '').strip() # ?
       # message_key = incoming_message.partition(" ")[0]

    
    if __name__ == "__main__":
        # For local development only; Gunicorn will be used in production
        app.run(debug=True, host="0.0.0.0", port=5000)
    
else:
    while True:
        try:
            message = testing_process_incoming()
            message_key = message[0]
            message_arguments = message[1]
            
            response = retrieve_response(message_key, message_arguments)
            print(f"TESTING_MODE: Sending message: {response}")  
    
        except KeyboardInterrupt:
            print("Exiting loop")
            break