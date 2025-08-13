import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from dotenv import load_dotenv
import os

# Gmail credentials
load_dotenv()
sender_email = os.getenv("email")
app_password = os.getenv("app_password")  # Use app password, not your regular password
receiver_email = "c2007hris@gmail.com"

# Email content
subject = "Test Email from Python"
body = "Hello team, hopefully this works if not I'm gonna cry."

# Create the message
message = MIMEMultipart()
message["From"] = sender_email
message["To"] = receiver_email
message["Subject"] = subject

# Attach the body
message.attach(MIMEText(body, "plain"))

# Send the email using Gmail's SMTP server
try:
    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
        server.login(sender_email, app_password)
        server.sendmail(sender_email, receiver_email, message.as_string())
    print("Email sent successfully!")
except Exception as e:
    print("Error sending email:", e)
