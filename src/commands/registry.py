import logging

registry = {}

def command(command_name: str):
    def decorator(func: str):
        registry[command_name] = func
        return func
    return decorator
        
    