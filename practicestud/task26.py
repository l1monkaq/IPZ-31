import requests

response_get = requests.get("https://httpbin.org/get", params={"user": "student"})
print(f"GET Status: {response_get.status_code}")
print(f"GET Headers: {response_get.headers.get('Content-Type')}")
print(f"GET Body: {response_get.json()['args']}")

data = {"item": "book", "qty": 1}
response_post = requests.post("https://httpbin.org/post", json=data)
print(f"\nPOST Status: {response_post.status_code}")
print(f"POST Result: {response_post.json()['json']}")