import requests
import json

token = "7629edd01fdbb13225e5ffed34449294"
github = "https://github.com/veganafro/api_challenge"
end_point = "http://challenge.code2040.org/api/register"

data = {'token': token,
        'github': github}

with open('results.json', 'w') as empty_json_file:
    json.dump(data, empty_json_file, indent=4)
    empty_json_file.close()

with open('results.json', 'rb') as full_json_file:
    json_data = json.load(full_json_file)
    full_json_file.close()

ret = requests.post(end_point, json=json_data)

print(ret.status_code)