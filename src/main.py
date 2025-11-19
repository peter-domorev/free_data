from helpers.process_incoming import process_incoming
from router import router
from validators.sms_validator import sms_validator
from helpers.error import error
import logging

logging.basicConfig(
    level=logging.CRITICAL + 1,
    format="%(asctime)s [%(levelname)s] %(funcName)s: %(message)s"
)


def main(raw_msg: str) -> str:




    # check:
    # auto reply after 30s
    # credit low for ai and twillio

    try:
        sms_validator.is_valid(raw_msg)
        cmd, args = process_incoming(raw_msg)
        response = router(cmd, args)
    except KeyError:
        response = error(f"\"{cmd}\" is not a valid command key")
    except TypeError:
        response = error(f"\"{args}\" is not a valid set of arguments")
    except NotImplementedError:
        response = error(f"{cmd} has not been implemented")
    except ValueError:
        response = error(f"Invalid characters used. Ensure characters are limited to:\n{sms_validator.allowed_characters}")
        
    return response

