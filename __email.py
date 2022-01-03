import smtplib, ssl

user = "email@gmail.com"
password = "password"

to = ["email@gmail.com"]
subject = f"Message from {user}"
message = "Hi, whats everything? \n\n"

email_text = """\
Subject:{}

{}
""".format(subject,message)

context = ssl.create_default_context()

with smtplib.SMTP_SSL("smtp.gmail.com",465, context=context) as server:
    server.login(user,password)
    server.sendmail(user,to,message)


#Note: For the password mail you will need to keep this instructions
# https://support.google.com/accounts/answer/185833?p=InvalidSecondFactor&visit_id=637679549018773838-2539989109&rd=1