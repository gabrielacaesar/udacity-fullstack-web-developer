from twilio.rest import Client

# SID da sua conta, encontre em twilio.com/console
account_sid = "ACbxxxxxxxxxx"
# Seu Auth Token, encontre em twilio.com/console
auth_token  = "e253a0dxxxxxxxxx"

client = Client(account_sid, auth_token)

message = client.messages.create(
    to="+5521xxx", 
    from_="+5541xxx",
    body="Hello world!")

print(message.sid)