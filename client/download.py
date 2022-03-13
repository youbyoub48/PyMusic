import requests, urllib.request, vlc, time

def Download():
    r = requests.get("http://127.0.0.1:8000/api")
    print(r.status_code)
    dico = r.json()

    for element in dico:
        musique = element
        urllib.request.urlretrieve(dico[musique], f"{musique}.mp3")

    p = vlc.MediaPlayer(f"{musique}.mp3")
    p.play()
    time.sleep(0.5)
    Millisecondes = p.get_length()
    Secondes = Millisecondes*0.001
    print(Secondes)
    time.sleep(Secondes)