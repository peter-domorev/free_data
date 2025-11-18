def idea_service(message_arguments):
    file_name = "ideas.txt"
    content_to_write = f'''Idea: {message_arguments}
    .
    '''
    
    with open(file_name, "a") as file:
        file.write(content_to_write)
    
    response = "Idea recorded to file"
    return response
