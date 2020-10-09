import smtplib          # Simple mail transfer protocol. Used to send emails to any internet machine.
import os               # Env variables.

EMAIL_ADDRESS = os.environ.get('D9_EMAIL_USER')     # Email address environment variable.

# You NEED to create app specific password for google. Your normal password wont work.
EMAIL_PASSWORD = os.environ.get('D9_EMAIL_PW')      # Email password environment variable.

conn = smtplib.SMTP('smtp.gmail.com', 587)

# Start connection
conn.ehlo()

# Start tls encryption, so when we send the password it will be encrypted.
conn.starttls()

# Logging in.
conn.login(EMAIL_ADDRESS, EMAIL_PASSWORD)

# Sending email
conn.sendmail(EMAIL_ADDRESS,'someones@email.com', 'Subject: So long...\n\nDear Asshole, \nSo long, and thanks for nothing.\n\n -D')

# Disconnect
conn.quit()
