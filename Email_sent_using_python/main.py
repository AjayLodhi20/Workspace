from email.message import EmailMessage
from datetime import datetime, timedelta
import smtplib
import time

msg = EmailMessage()

msg["subject"] = "Birthday message"
msg["from"] = "satyamlodhi123@gmail.com"
msg["to"] = "satyamlodhi735562@gmail.com"
msg.set_content("Wishing you a fantastic birthday!")

target_time = datetime.now() + timedelta(seconds=20)

time_left = target_time - datetime.now()

seconds_to_wait = time_left.total_seconds()

if seconds_to_wait > 0:
    print(f"Waiting {seconds_to_wait} seconds to send...")
    time.sleep(seconds_to_wait)
else:
    print("sending immediately")

with smtplib.SMTP("smtp.gmail.com", 587) as server:
        server.starttls() #encrypts the message
        server.login("satyamlodhi123@gmail.com", 'uire emja eexd sgwg')
        server.send_message(msg)

print("Email sent!")