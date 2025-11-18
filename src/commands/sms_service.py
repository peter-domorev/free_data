def sms_service(message_arguments):
    to_phone_number = message_arguments.partition(" ")[0]
    send_message = message_arguments.partition(" ")[2]


    client = Client(account_sid, auth_token)
    client.messages.create(
        body=send_message,
        from_=twilio_number,
        to=to_phone_number
    )

    # could be used for verifying a phone number
    #from_number = request.form.get('From')


    response = f"Message successfully sent to {to_phone_number}"
    return response