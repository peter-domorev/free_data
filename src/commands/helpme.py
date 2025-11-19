import logging
from .registry import registry, register
from .icommand import ICommand

@register("helpme")
class HelpMe(ICommand):
    
    helpme_syntax = "helpme [command]"
    
    helpme_guide = NotImplementedError
    
    
    def response(args: str):
    
        commands_syntax = []
        for obj in registry: commands_syntax.append(registry[obj].helpme_syntax)
        
        
        return str(commands_syntax) 

