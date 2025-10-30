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

