import requests

req = requests.get('http://resources.infosecinstitute.com/')
print 'Response Code: ' + str(req.status_code)
print '\nResponse:\n' + req.text
