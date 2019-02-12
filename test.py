import re

phoneNumRegex = re.compile(r'(\(\d\d\d\)) (\d\d\d-\d\d\d\d)')

mo = phoneNumRegex.search('My number is (415) 555-4242.')

print("My phone number is: " + mo.group(1))
