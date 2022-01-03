import jwt


# ======================Encoded Token================
data = {"some": "payload"}

encode_jwt = jwt.encode(data,
                        "secret", algorithm="HS256")

print("------------Encoded Token------------\n")
print(encode_jwt)
print("----------------------------------------\n")

# ======================Decoded Token================
decode_jwt = jwt.decode(encode_jwt, "secret", algorithms="HS256")


print("------------Decoded Token------------\n")
print(decode_jwt)
print("----------------------------------------\n")


# token = "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyIjoiam9zZSIsImxhc3RuYW1lIjoiZW5jYXJuYWNpb24ifQ.l5YbNoNMSCrtzxpndXdnuXH1Y2S0trepwZRcNCyqbw8"

# decode_jwt = jwt.decode(token,"secret",algorithms="HS256")

# The Json Web Token(JWT) are used to secure the apis

# Example give authorization to a user, information exchange etc.

# It have three parts the Header,Payload and Signature.

# The header typically consists of two parts: the type
# of the token, which is JWT, and the signing algorithm
# being used, such as HMAC SHA256 or RSA.


# The second part of the token is the payload, which
# contains the claims. Claims are statements about an
# entity (typically, the user) and additional data.
# There are three types of claims: registered, public,
# and private claims.

# To create the signature part you have to take the
# encoded header, the encoded payload, a secret,
# the algorithm specified in the header, and sign
# that.

# print("----------Token Decoded-----------------\n")
# print(decode_jwt)
# print("----------------------------------------\n")
