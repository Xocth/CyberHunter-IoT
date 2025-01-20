import requests

url = "127.0.0.1:8080/scores"
response = requests.get(url)

if response.status_code == 200:
    with open("scores.txt", "wb") as file:
        file.write(response.content)
    print("File downloaded successfully!")
else:
    print("Failed to download the file.")
