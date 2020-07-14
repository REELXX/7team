import json,jsonpath
import requests

api_url ='https://192.168.56.101/restconf/data/ietf-interfaces:interfaces'
header = {
                'accept': 'application/yang-data+json',
                'content-type': 'application/yang-data+json'
            }
basic_auth = ('cisco', 'cisco123!')
resp = requests.get(api_url, auth=basic_auth, headers=header, verify=False)
response_json = resp.json()
name = jsonpath.jsonpath(response_json,'$..type')
print(name)
#print(json.dumps(response_json,indent=4))

# def get_oneinfo(json,gongneng):
#     response_json = json.json()
#     shixian = gongneng
#     output = jsonpath.jsonpath(response_json,f'$..{shixian}')
#     print(output)
# get_oneinfo(resp,enable)