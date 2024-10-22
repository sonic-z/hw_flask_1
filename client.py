import requests

#
# response = requests.post("http://127.0.0.1:8000/advertisement/",
#                          json={
#                              "title": "title2222",
#                              "description": "description22",
#                              "price": 888,
#                              "author": "admin"
#
#                          }
#                          )

# response = requests.patch("http://127.0.0.1:8000/advertisement/3", json={'price': 100000})
# print(response.status_code)
# print(response.json())
#
# response = requests.delete("http://127.0.0.1:8000/advertisement/1")
# print(response.json())


#response = requests.get("http://127.0.0.1:8000/advertisement/3")
# print(response.json())

response = requests.get("http://127.0.0.1:8000/advertisement/", params={"query_string": "title"})
print(response.json())

response = requests.get("http://127.0.0.1:8000/advertisement/?query_string=title")
print(response.json())
# print(response.json())