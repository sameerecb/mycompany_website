# link to create app passwords https://myaccount.google.com/apppasswords"
import smtplib
import ssl


def send_email(message):
    host = "smtp.gmail.com"
    port = 465
    username = "theflexfound@gmail.com"
    password = "cfcooyaokacnnwyh"
    receiver = "theflexfound@gmail.com"  # Chane to different email address where you want to receive email.
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL(host, port, context=context) as server:
        server.login(username, password)
        server.sendmail(username, receiver, message)


