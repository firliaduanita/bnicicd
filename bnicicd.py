import requests

print("Hello World!")
print("Halooo lagi")

response = requests.get("https://www.google.com")

print (response.text)