import sys
import json
import requests

list_ = sys.argv[1:]
host = list_[0]
port = list_[1]
witchcrafts = list_[2:]

positive_arg = 4
odd_flag = False

if "--positive" in witchcrafts:
    index = sys.argv.index("--positive")
    positive_arg = int(sys.argv[index + 1])

if "--odd" in sys.argv:
    odd_flag = True

response = requests.get(f'http://{host}:{port}')
data = json.loads(response.text)