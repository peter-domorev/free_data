import logging




class sms_validator:
    allowed_characters = "abcdefghijklmnopqrstuvwxyz\nABCDEFGHIJKLMNOPQRSTUVWXYZ\n0123456789\n!@#$%^&*()_-+=;:'\"/,.?[]{} "
    
    def is_valid(sms: str):
    
        is_valid = all(c in set(sms_validator.allowed_characters) for c in sms)
        
        if not is_valid: raise ValueError
