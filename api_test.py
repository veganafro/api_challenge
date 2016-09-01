import requests
import json

token = "7629edd01fdbb13225e5ffed34449294"

def challenge_1():
    github = "https://github.com/veganafro/api_challenge"
    end_point = "http://challenge.code2040.org/api/register"

    data = {'token': token,
            'github': github}

    write_json_file('results.json', data)

    python_style_json = convert_json_file('results.json')

    ret = requests.post(end_point, json=python_style_json)
    print(ret.status_code)



def challenge_2():
    start_point = "http://challenge.code2040.org/api/reverse"
    end_point = "http://challenge.code2040.org/api/reverse/validate"

    data = {'token': token,
            'string': ""}

    write_json_file('results_2.json', data)
    python_style_json = convert_json_file('results_2.json')

    first_ret = requests.post(start_point, json=python_style_json)

    python_style_json['string'] = first_ret.content[::-1]
    write_json_file('results_2.json', python_style_json)

    second_ret = requests.post(end_point, json=python_style_json)
    print(second_ret.status_code)



def challenge_3():
    start_point = "http://challenge.code2040.org/api/haystack"
    end_point = "http://challenge.code2040.org/api/haystack/validate"

    python_style_json = convert_json_file('results_2.json')

    first_ret = requests.post(start_point, json=python_style_json)

    dictionary = json.loads(first_ret.content)

    needle = dictionary.get('needle')
    location_of_needle = dictionary.get('haystack').index(needle)

    python_style_json['needle'] = location_of_needle
    write_json_file('results_2.json', python_style_json)

    second_ret = requests.post(end_point, json=python_style_json)
    print(second_ret.status_code)



def challenge_4():
    start_point = "http://challenge.code2040.org/api/prefix"
    end_point = "http://challenge.code2040.org/api/prefix/validate"

    python_style_json = convert_json_file('results_2.json')

    first_ret = requests.post(start_point, json=python_style_json)

    dictionary = json.loads(first_ret.content)

    prefix = dictionary.get('prefix')

    non_matches = []

    for string in dictionary.get('array'):
        if prefix != string[:len(prefix)]:
            non_matches.append(string)

    python_style_json['array'] = non_matches
    write_json_file('results.json', python_style_json)

    second_ret = requests.post(end_point, json=python_style_json)
    print(second_ret.status_code)



def write_json_file(filename, python_dict):
    with open(filename, 'w') as empty_json_file:
        json.dump(python_dict, empty_json_file, indent=4)
        empty_json_file.close()

def convert_json_file(filename):
    with open(filename, 'rb') as full_json_file:
        json_data = json.load(full_json_file)
        full_json_file.close()
        return json_data



#challenge_1()
#challenge_2()
#challenge_3()
challenge_4()