import logging

def sms_is_valid(sms: str) -> bool:
    allowed_characters = set(
        "abcdefghijklmnopqrstuvwxyz"
        "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        "0123456789"
        "!@#$%^&*()_-+=;:'\"/,.?[]{}"
        )
    
    is_valid = all(c in allowed_characters for c in sms)
    
    return is_valid