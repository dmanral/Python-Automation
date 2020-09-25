#! python3
import re
import pyperclip

# TODO: Create a regex for phone numbers
phoneRegex = re.compile(r''' 
# 415-555-000, 555-0000, (415) 555-000, 555-0000 ext 12345, ext. 12345, x12345
(
((\d\d\d) | (\(\d\d\d\)))?      # area code(optional)
(\s | -)        # first separator
\d\d\d        # first 3 digits
-        # separator
\d\d\d\d        # last 4 digits
(((ext(\.)?\s)|x)       # extension word-part (optional)
 (\d{2,5}))?            # extension number-part (optional)
)
''', re.VERBOSE)

# TODO: Create a regex for email addresses
emailRegex = re.compile(r'''
[a-zA-z0-9_.+]+  # name part
@    # at symbol
[a-zA-z0-9_.+]+    # domain name part
''', re.VERBOSE)

# TODO: Get the text off the clipboard.0
text = pyperclip.paste()

# TODO: Extract the email/phone from this text
extratedPhone = phoneRegex.findall(text)
extratedEmail = emailRegex.findall(text)

allPhoneNumbers = []
for phoneNumber in extratedPhone:
    allPhoneNumbers.append(phoneNumber[0])

# print(allPhoneNumbers)

# TOdo: Copy the extracted email/phone to the clipboard
results = '\n'.join(allPhoneNumbers) + '\n' + '\n'.join(extratedEmail)
pyperclip.copy(results)