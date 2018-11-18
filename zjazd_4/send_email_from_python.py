import smtplib

user = "python"
password = ""

sent_from = "python@wp.pl"
to =["ms@wp.pl"]
subject = "Try this"
body = "To jest tersc"

email_txt = f"""
From: {sent_from}
To: {','.join(to)}
Subject: {subject}

{body}
"""

try:
    server = smtplib.SMTP_SSL

except Exception as e:
    print(e)
    print("Coś poszło źle")
    with open("bledy.txt", "w")