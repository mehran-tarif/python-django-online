# import random

# num = random.randrange(, 10)
# num = random.randint(0, 10)
# print(num)

# from datetime import datetime

# print(datetime.now)
import json
# mystr = '{"name": "mehran"}'
# j = json.loads(mystr)
# print(j.get('name'))
# print(type(j))
import requests

data = requests.get("https://api.nasa.gov/planetary/apod?api_key=DEMO_KEY").content
data = json.loads(data)

print(data.get('hdurl'))