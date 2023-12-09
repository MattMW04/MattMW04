import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def send(subject, body, to_email):
    user = 'matt.wilcox24.2@gmail.com'
    pasw = 'Cairn107#'
    server = 'smtp.gmail.com'
    email_port = 587

    #create message
    msg = MIMEMultipart()
    msg['From'] = user
    msg['To'] = to_email
    msg['Subject'] = subject

    msg.attach(MIMEText(body, 'plain'))

    # set up server
    with smtplib.SMTP(server,email_port) as server:
        server.starttls()
        server.login(user, pasw)
        server.send_message(msg)




subject = "Tom is obese"
body = "peepee"
email = "matt.wilcox24.1@gmail.com"

send(subject,body,email)
