import logging
from commands.registry import registry

def router(cmd: str, args: str) -> str:
    obj = registry.get(cmd)
    
    if obj is None: raise KeyError
    
    response = obj.response() if args is None else obj.response(args)
    
    return response