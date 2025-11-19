import logging

registry = {}

def register(name: str):
    def decorator(obj):
        registry[name] = obj
        return obj
    return decorator
        

