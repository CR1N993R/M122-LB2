import datetime
import smtplib
import ssl
from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from configparser import ConfigParser


def send_to_email(receiver, filename):
    if len(receiver) == 0:
        return
    parser = ConfigParser()
    parser.read("../config.ini")
    sender = parser.get("Gmail SMTP", "email")
    message = MIMEMultipart()
    message["From"] = sender
    message["To"] = receiver
    message["Subject"] = "Report " + filename

    message.attach(MIMEText("This report was Created at " + datetime.datetime.now().strftime("%m/%d/%Y, %H:%M:%S"), "plain"))
    filename = filename
    with open(filename, "rb") as attachment:
        part = MIMEBase("application", "octet-stream")
        part.set_payload(attachment.read())
    encoders.encode_base64(part)

    part.add_header(
        "Content-Disposition",
        f"attachment; filename= {filename}",
    )

    message.attach(part)
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
        server.login("cedric.ringger.dev@gmail.com", parser.get("Gmail SMTP", "password"))
        server.sendmail(sender, receiver, message.as_string())
