import requests, urllib.request, os

r = requests.get("http://127.0.0.1:8000/api")
print(r.status_code)
dico = r.json()

for element in dico:
    musique = element
    urllib.request.urlretrieve(dico[musique], f"{musique}.mp3")

os.system(f"{musique}.mp3")