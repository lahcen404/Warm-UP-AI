import requests

url = "https://jsonplaceholder.typicode.com/users"
response = requests.get(url)
users =response.json()

for usr in users:
    print(usr["name"])
    print(usr["address"]["city"])
    print("-------------")
    
# headers = {"Accept": "application/json"}
#response = requests.get(url, headers=headers)

# POST

data = {
    "title": "Learning Python APIs",
    "body": "I am practicing requests",
    "userId": 1
}

response = requests.post(url, json=data)


# PUT
data = {
    "id": 1,
    "title": "New title",
    "body": "New content",
    "userId": 1
}

response = requests.put(
    "https://jsonplaceholder.typicode.com/posts/1",
    json=data
)

# PATCH

data = {
    "title": "New title"
}

response = requests.patch(
    "https://jsonplaceholder.typicode.com/posts/1",
    json=data
)

# DELETE

response = requests.delete(
    "https://jsonplaceholder.typicode.com/posts/1"
)

