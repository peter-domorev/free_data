from helpers.process_incoming import process_incoming
from router import router
from commands import ai
from validators.sms_is_valid import sms_is_valid
from helpers.error import error

raw_msg = "al tell me a joke"
cmd, args = process_incoming(raw_msg)



# validation testing
if not sms_is_valid(raw_msg):
    print("not valid")


# check:
# auto reply after 30s
# credit low for ai and twillio




print(cmd)
print(args)

try:
    response = router(cmd, args)
except KeyError:
    error_msg = f"\"{cmd}\" is not a valid command key"
    response = error(error_msg)




print(response)