#%%
import json

#%%
people = ''' [
  {
    "age": 29,
    "eyeColor": "brown",
    "name": "Bernadine Moses",
    "gender": "female"
  },
  {
    "age": 28,
    "eyeColor": "brown",
    "name": "Wilcox Conner",
    "gender": "male"
  },
  {
    "age": 22,
    "eyeColor": "brown",
    "name": "Alice Spencer",
    "gender": "female"
  },
  {
    "age": 23,
    "eyeColor": "green",
    "name": "Cooley Miller",
    "gender": "male"
  },
  {
    "age": 38,
    "eyeColor": "blue",
    "name": "Thomas Vargas",
    "gender": "male"
  },
  {
    "age": 39,
    "eyeColor": "brown",
    "name": "Simpson Jackson",
    "gender": "male"
  },
  {
    "age": 20,
    "eyeColor": "blue",
    "name": "Bentley Ortega",
    "gender": "male"
  }

]

'''
#%%

# if you have json data as a string use json.loads
data = json.loads(people)

for person in data:
    print(person['age'])

#%%

# we can dump the data in json
for person in data:
    del person['age']

new_string = json.dumps(data, indent=2, sort_keys=True)
print(new_string)

#%%

# to load the file you can use json.load

with open('json_module/states.json') as f:
    data = json.load(f)

#adding new key and value to the json
for states in data['states']:
    states['pin_code'] = 234214124

# to remove the key
for states in data['states']:
    del states['pin_code']

# dumping the data with indentation
with open('new_states.json', 'w') as f:
    json.dump(data, f, indent=2)

#%%
import requests

response = requests.get(r'https://json-ld.org/contexts/person.jsonld')

if response.ok:
    data = response.text
    data = json.loads(data) # since data is a string
    print(json.dumps(data, indent=2))

    print(type(data))

response.close()

