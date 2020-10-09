import imapclient
import pyzmail

conn = imapclient.IMAPClient('imap.gmail.com', ssl=True)

# Loginto email, again you will need to create app only password for google.
conn.login('email', 'password')

# Usually inbox and readonly so you dont accidently delete emails.
# To delete set readonly to false.
conn.select_folder('INBOX', readonly=True)

# Search email; returns list of unique IDs for all emails found.
# Imap has their own particular syntax for searching.
UIDs = conn.search('[SINCE 20-Aug-2020]')

# To delete
# conn.delete_messages([UIDs[1]])

# Actually see the message.
rawMessage = conn.fetch([UIDs[9]], ['BODY[]', 'FLAGS'])

# Clean view of the message.
message = pyzmail.PyzMessage.factory(rawMessage[UIDs[9]][b'BODY[]'])

# Get individual email items.
message.get_subject()
message.get_addresses('from')

# Check if message just has text part.
message.text_part

# See body
print(message.text_part.get_payload().decode('UTF-8'))

# Logout
conn.logout()
