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

doql_api = '/services/data/v1.0/query/?query=SELECT * FROM view_device_v1 order by device_pk'
url = D42_URL+doql_api
response = requests.get(url,headers=headers, verify=False)

is_baseline = raw_input("Is baseline: ")
if is_baseline.lower() == 'yes':
    target = open('device_baseline.d42', 'w')
    target.write( response.content )
    print 'baseline created'
else:
    target = open('device_baseline.d42', 'r')
    old_content = target.read()
    if response.content == old_content:
        print 'old and new identical'



