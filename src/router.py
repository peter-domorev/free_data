import logging
from commands.registry import registry

def router(cmd: str, args: str) -> str:
    func = registry.get(cmd)
    
    if func is None: raise KeyError
    
    response = func(args) # re structure how registry has classes, not functions
    
    return response