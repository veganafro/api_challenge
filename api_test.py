import requests
import json
import threading
import datetime
import iso8601
import os

# define the global token variable that will need to be posted on each call to the API
token = os.environ["API_TOKEN"]

thread_lock = threading.Lock()

class ThreadSolver(threading.Thread):

    def __init__(self, thread_id, method_to_run):
        threading.Thread.__init__(self)
        self.thread_id = thread_id
        self.method_to_run = method_to_run

    def run(self):
        print("Starting thread " + str(self.thread_id))
        thread_lock.acquire()
        self.method_to_run()
        thread_lock.release()

def challenge_1():
    github = "https://github.com/veganafro/api_challenge"
    end_point = "http://challenge.code2040.org/api/register"

    data = {'token': token,
            'github': github}

    write_json_file('results_2.json', data)

    python_style_json = convert_json_file('results_2.json')

    ret = requests.post(end_point, json=python_style_json)
    print(ret.status_code)

def challenge_2():
    start_point = "http://challenge.code2040.org/api/reverse"
    end_point = "http://challenge.code2040.org/api/reverse/validate"

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
    write_json_file('results_2.json', python_style_json)

    second_ret = requests.post(end_point, json=python_style_json)
    print(second_ret.status_code)

def challenge_5():
    start_point = "http://challenge.code2040.org/api/dating"
    end_point = "http://challenge.code2040.org/api/dating/validate"

    python_style_json = convert_json_file('results_2.json')

    first_ret = requests.post(start_point, json=python_style_json)

    dictionary = json.loads(first_ret.content)

    date_stamp = dictionary.get('datestamp')
    interval = dictionary.get('interval')

    date_with_delta = iso8601.parse_date(date_stamp) + datetime.timedelta(seconds=interval)

    # bootleg solution to the issue of the isoformat() method returning +00:00 instead of Z for the time-zone
    python_style_json['datestamp'] = date_with_delta.isoformat()[:len(date_with_delta.isoformat()) - 6] + "Z"
    write_json_file('results_2.json', python_style_json)

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


thread_one = ThreadSolver(1, challenge_1)
thread_two = ThreadSolver(2, challenge_2)
thread_three = ThreadSolver(3, challenge_3)
thread_four = ThreadSolver(4, challenge_4)
thread_five = ThreadSolver(5, challenge_5)

thread_one.start()
thread_two.start()
thread_three.start()
thread_four.start()
thread_five.start()