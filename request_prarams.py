import requests

r = requests.get('https://google.com')

print(r.content)
print(type(r.content))
print(r.text)
print(r.encoding)
# --ISO-8859-1---
r.encoding = 'utf-8'
# change ncoding to utf-!
print(r.encoding) # encoding is now changed to - utf-8