import logging
from .ai import ai
from .registry import registry
from .icommand import ICommand

class HelpMe(ICommand):
    
    helpme_syntax = "helpme [command]"
    
    helpme_guide = "Not implemented"
    
    
    def helpme():
    
        commands_syntax = []
        for obj in registry: commands_syntax.append(obj.helpme_syntax)
        
        
        return str(commands_syntax) 

