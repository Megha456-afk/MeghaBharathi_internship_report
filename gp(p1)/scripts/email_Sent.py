import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# =========================
# EMAIL DETAILS
# =========================
from_email = "meghabharathi109@gmail.com"
app_password = "dcolhjmarreofylf"   # Gmail app password

to_email = from_email
subject = "Today's FINAL_SORTED.FILE"

body = """
Hello,

The bot has ran successfully
and been given the final sorted file 
with all the updated files.

Thank you,
Megha Bharathi M
"""

# =========================
# BUILD EMAIL
# =========================
msg = MIMEMultipart()
msg["From"] = "Megha Bharathi <meghabharathi109@gmail.com>"
msg["To"] = to_email
msg["Subject"] = "Daily File Update"
msg.add_header("Reply-To", from_email)
msg.add_header("X-Mailer", "Python SMTP")

msg.attach(MIMEText(body, "plain"))


# =========================
# SEND EMAIL
# =========================
try:
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login(from_email, app_password)

    server.send_message(msg)
    server.quit()

    print(" Email sent successfully!")

except Exception as e:
    print("Failed to send email:", e)
server = smtplib.SMTP("smtp.gmail.com", 587)
server.set_debuglevel(1)
server.starttls()
server.login(from_email, app_password)
server.send_message(msg)
server.quit()
