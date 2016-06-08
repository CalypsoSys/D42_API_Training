import sys
import requests
import base64

try:
    requests.packages.urllib3.disable_warnings()
except:
    pass

D42_USER    = 'admin'
D42_PWD     = 'adm!nd42'
D42_URL     = 'http://localhost:8000'


headers = {
            'Authorization': 'Basic ' + base64.b64encode(D42_USER + ':' + D42_PWD),
            'Content-Type': 'application/x-www-form-urlencoded'
        }

f = '/api/1.0/devices/'
url = D42_URL+f
response = requests.get(url,headers=headers, verify=False)
raw = response.json()

devices = [x['device_id'] for x in raw['Devices']]
total = len(devices)
i = 1
for device in devices:
    print '\t[-] Device ID: %s [%d of %d]' % (device, i, total)
    f = '/api/1.0/devices/%s/' % device
    url = D42_URL + f
    i+=1
