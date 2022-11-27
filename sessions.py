import requests
session = requests.Session()

response = requests.get("https://google.co.in", cookies={"new-cookieidentifier":"1234abcd"})
print(response)
print(response.request.headers)
#<Response [200]>
#{'User-Agent': 'python-requests/2.26.0', 'Accept-Encoding': 'gzip, deflate', 'Accept': '*/*', 
#'Connection': 'keep-alive', 'Cookie': 'new-cookieidentifier=1234abcd; CONSENT=PENDING+291'} 

print(response.request.headers['Cookie'])
# ----  new-cookieidentifier=1234abcd; CONSENT=PENDING+623
print(response.url)
# ---https://www.google.co.in/

print(response.elapsed)
# -- 0:00:00.175696

print(response .reason)
#OK


""" Specifying Default values
With session object, we can specify some default values of the properties,
which needs to be sent to the server using GET, POST, PUT
"""
# session.paams = {"key1": "value", "key2": "value2"}
# session.auth = {'username': 'password'}
# session_header = session.headers.update({'foo': 'bar'})
# print(session_header)