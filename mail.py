import re

text = "Contact us at raj@gmail.com or support@example.com"

pattern = r'\w+@\w+\.\w+'

emails = re.findall(pattern, text)

print("Email addresses found:")
for email in emails:
    print(email)
