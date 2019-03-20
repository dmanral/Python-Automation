import os       # Environment variables b/c email and pass is stored elsewhere.
import smtplib  # Simple mail transfer protocol. Used to send emails to any internet machine.
import imghdr   # Helps with multiple image attachments and helps determine what type of image.
from email.message import EmailMessage  # EmailMessage is an object that makes it easier to format emails.

EMAIL_ADDRESS = os.environ.get('EMAIL_USER')    # Email address environment variable.
EMAIL_PASSWORD = os.environ.get('EMAIL_PASS')   # Email password environment variable.

contacts = ['yourcontactemail@whatever.com']          # Add comma and more emails.

# Emails informations:
msg = EmailMessage()
msg['Subject'] = 'Blahbity blah blah'
msg['From'] = EMAIL_ADDRESS
msg['To'] = ', '.join(contacts)
msg.set_content('This is a plain text email.')

# For HTML email: (You can make your email prettier if you like.)
msg.add_alternative("""\
<!DOCTYPE>
<html>
    <body>
        <h1 style="color:SlateGray;"> This is an HTML email.</h1>
    </body>
</html>
""", subtype='html')


# Multiple image files:
# files = ['Incredible-Hulk-Wallpaper.jpg', 'hulk-wallpaper-Smash.jpg', 'The-Hulk-Wallpaper.jpg']

# For Pdf files:
# files = ['resume.pdf']

# Multi email attachment.
# for file in files:
#     with open(file, 'rb') as f:
#         file_data = f.read()
#         file_type = imghdr.what(f.name) # Don't need this for pdf.
#         file_name = f.name
#     msg.add_attachment(file_data, maintype='image', subtype=file_type, filename=file_name)
    # For pdf:
    # msg.add_attachment(file_data, maintype='application', subtype='octet-stream', filename=file_name)

# Single Email attachment.
# with open('Incredible-Hulk-Wallpaper.jpg', 'rb') as f:
#     file_data = f.read()
#     file_type = imghdr.what(f.name)
#     file_name = f.name

# msg.add_attachment(file_data, maintype='image', subtype=file_type, filename=file_name)

with smtplib.SMTP_SSL('smtp.gmail.com', 465)as smtp:   # This is only for google.

    # How you login.
    smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)

    # smtp.send_message(message)
    smtp.send_message(msg)
