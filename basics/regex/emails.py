import re

emails = '''
JhonJenks@gmail.com
jhon.jenks@university.edu
jhon-23+-jenks@my-work.net
'''

pattern = re.compile(r'[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+')

matches = pattern.finditer(emails)

for match in matches:
    print(match)
