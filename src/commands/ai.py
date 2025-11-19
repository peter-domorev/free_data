import ollama
from .registry import register
from .icommand import ICommand

@register("ai")
class AI(ICommand):
    cmd = "ai"
    
    helpme_syntax = "ai <prompt>"
    
    helpme_guide = NotImplementedError
    
    def response(prompt: str):
        
        raise NotImplementedError
        
        return
    
    


