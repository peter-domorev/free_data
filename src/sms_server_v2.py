import ollama
#from annotated_types.test_cases import cases
from twilio.rest import Client
from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse
import subprocess
import re

# version 2
TESTING_MODE = True





# response functions
def ai_response(message_arguments):
    import ollama

    response = ollama.chat(
        model='gemma3n',
        messages=[{'role': 'user', 'content': message_arguments}],
        options={'num_predict': 4/3 * 100}) # 4/3 words is 1 token
    
    response = response.message.content
    

    def strip_markdown(text):
        # Remove bold and italic markers like **text**, *text*, __text__, _text_
        text = re.sub(r'(\*\*|__)(.*?)\1', r'\2', text)
        text = re.sub(r'(\*|_)(.*?)\1', r'\2', text)
        # Remove bullets and leading whitespace
        text = re.sub(r'^\s*[-*+]\s+', '', text, flags=re.MULTILINE)
        # Optional: remove headers like ## Title
        text = re.sub(r'^#{1,6}\s+', '', text, flags=re.MULTILINE)
        return text
   
   
    response = strip_markdown(response)
   
    return response

def maps_response():
    response = "function still in development"
    return response

def sms_external(message_arguments):
    to_phone_number = message_arguments.partition(" ")[0]
    send_message = message_arguments.partition(" ")[2]


    client = Client(account_sid, auth_token)
    client.messages.create(
        body=send_message,
        from_=twilio_number,
        to=to_phone_number
    )

    # could be used for verifying a phone number
    #from_number = request.form.get('From')


    response = f"Message successfully sent to {to_phone_number}"
    return response
    
def idea_response(message_arguments):
    file_name = "ideas.txt"
    content_to_write = f'''Idea: {message_arguments}
    .
    '''
    
    with open(file_name, "a") as file:
        file.write(content_to_write)
    
    response = "Idea recorded to file"
    return response

def prank_response():
    '''phone_number = arguments.partition(" ")[0]
    name = arguments.partition(" ")[2]

    print("Listen carefuly", name, ", over the next 5 minutes, you will recieve a series of texts with"
                                   "instructions of what I want you to do")
    print("Failure to cooperate could mean humourous consequences")
    print("I would like you to make you hand flat, fingers together")
    print("Now point you arm directly up")
    print("Lower it slightly")
    print("A little more")
    print("Stop when you get to roughly 45 degrees")
    print("Now on you other hand make a pointing shape")
    print("Now put it above your mouth as if it was a moustache")'''

    response = "function still in development"
    return response

def helpme_response():
    response = \
    """ 
    general syntax: function_key <arguments>
    
    Functions:
    ai <prompt> 
    maps <directions>
    text (or sms_external?) <phone_number> <message> 
    idea <content>
    prank <phone_number>
    helpme
    nine11
    verify
    shutdown
    """

    return response

def nine11_response():
    
    response = "Function still in development"
    
    print("nine11")
    
    return response
        
def verify_phone(message_arguments):
    
    
    
    '''print("verify")
    
    to_phone_number = message_arguments.partition(" ")[0]
    send_message = message_arguments.partition(" ")[2]
    
    
    from_number = request.form.get('From')
    
    


    client = Client(account_sid, auth_token)
    message = client.messages.create(
        body=send_message,
        from_=twilio_number,
        to=to_phone_number
    )

    '''
    
    
    
    
    
    
    
    response = 'function still in development'
    return response

def shutdown_pi():
    #    subprocess.run(['sudo', 'shutdown', '-h', 'now'])
    # need layers of verification, so only I can do it, or maybe hard wire it for my own phone

    response = 'function still in development'
    return response


# dictionary code
'''
# Conversation storage (in-memory dictionary)
conversation_history = {}

# functions for in the response block

# Simple example: echo back the message and store history
    history = conversation_history.setdefault(from_number, [])
    history.append(f"User: {body}")

# Store the reply too
    history.append(f"AI: You said: {body}")'''



# messaging functions
def testing_process_incoming():
    incoming_message = input("TESTING_MODE: Incoming message: ")
    message_key = incoming_message.partition(" ")[0]
    message_arguments = incoming_message.partition(" ")[2]

    return [message_key, message_arguments]


def process_incoming():
    incoming_message = request.form.get('Body', '').strip()
    print(f"Incoming message: {incoming_message}")
    message_key = incoming_message.partition(" ")[0]
    message_arguments = incoming_message.partition(" ")[2]
    
    return [message_key, message_arguments]

def retrieve_response(message_key, message_arguments):
    match message_key:
        case "ai":
            response = ai_response(message_arguments)
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
            
    print(f"Successfully created response for: {message_key}")
    return response

def process_outgoing(response):
    response = f"{message_key}\n\n{response}"
    response_object = MessagingResponse()
    response_object.message(response)
    print(f"Sending message: {response}")
    return str(response_object)


# full app together
if not TESTING_MODE:
    app = Flask(__name__)
    
    @app.route("/sms", methods=["POST"])
    def sms_reply():
        message = process_incoming()
        message_key = message[0]
        message_arguments = message[1]
        
        response = retrieve_response(message_key, message_arguments)           
        return process_outgoing(response)
    
    
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