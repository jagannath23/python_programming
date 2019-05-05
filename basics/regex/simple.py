import re

"""
something to clear out
print('\thii')
print(r'\thii')
"""

text_to_search = '''
abcdefghijklmnopqrstuvwxyz
ABCDEFGHIJKLMNOPQRSTUVWXYZ
1234567890

ja jaja

MetaCharacters (Need to be escaped):
. ^ $ * + ? { } [ ] \ | ( )

multinexo.com

20-39601018-7
192.168.0.1

Mr. Jenks
Mr Smith
Ms Davis
Mrs. Robinson
Mr. T
'''

sentence = 'Writing our first regular expression'

# cuit regex
# pattern = re.compile(r'\d{2}-\d{8}-\d')
# ip regex
# pattern = re.compile(r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}')
pattern = re.compile(r'M(r|s|rs)\.?\s[A-Z]\w*')


matches = pattern.finditer(text_to_search)

for match in matches:
    print(match)

