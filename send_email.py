import smtplib, ssl


def send_email(message):
    host = "smtp.gmail.com"
    port = 465

    user_name = "abdulrehmanikram9@gmail.com"
    password = "iqdh kuth jmfb iwjn"
    #iqdh kuth jmfb iwjn

    context = ssl.create_default_context()

    receiver = "abdulrehmanikram9@gmail.com"

    with smtplib.SMTP_SSL(host, port, context=context) as server:
        server.login(user_name, password)
        server.sendmail(user_name, receiver, message )

