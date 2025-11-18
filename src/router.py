import logging
from registry import registry

def router(cmd: str, args: str) -> str:
    func = registry.get(cmd)
    
    if func is None: raise KeyError(cmd, "Function not found")
    
    response = func(args)
    
    return response