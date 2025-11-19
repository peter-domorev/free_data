import logging

def process_incoming(msg: str) -> list:
    
    split_msg = msg.split(" ", maxsplit=1)
    
    cmd = split_msg[0]
    args = split_msg[1] if len(split_msg) > 1 else None
    
    logging.info(f"Message processed. cmd: {cmd}, args {args}")
    
    return cmd, args