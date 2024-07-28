# 94. Sending Email using python[10:01:12]----------------------------------------------
import smtplib
sender = "u2003016@student.cuet.ac.bd"
receiver= "mahird.chowdhury@gmail.com"
password = "raop jhra qadc yisj"
subject="Python Email test"
body = "I wrote an email! :D"

# Header
message=f"""From: CUETIAN Dhiyan{sender}
To: Mahir Dhiyan {receiver}
Subject: {subject}\n 
{body}
"""
try:
    server=smtplib.SMTP("smtp.gmail.com",587)
    server.starttls()
    server.login(sender,password)
    print("Logged in")
    server.sendmail(sender,receiver,message)
    print("Email has been sent!")
except smtplib.SMTPAuthenticationError:
    print("Unable to sign in")

