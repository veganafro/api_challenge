import requests
import json

token = "7629edd01fdbb13225e5ffed34449294"
github = "https://github.com/veganafro/api_challenge"
end_point = "http://challenge.code2040.org/api/register"

data = {'token': token,
        'github': github}

with open('result.json', 'w') as fp:
    json_data = json.dump(data, fp, indent=4, sort_keys=False)

ret = requests.post(end_point, json=json_data)