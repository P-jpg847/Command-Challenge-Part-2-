import base64

#encoded string
encoded_string = ("Q29tbWFuZCBMaW5lIENoYWxsZW5nZSBQeXRob24gUGFydCAy==")

#decoding stuff
decoded_bytes = base64.b64decode(encoded_string).decode('utf-8')
print(decoded_bytes)
