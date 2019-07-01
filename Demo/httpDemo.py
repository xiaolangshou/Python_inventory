import requests

resp = requests.get('http://www.whatismybrowser.com')

f = open('1.log','w')
f.write(resp.text)

f.close()


