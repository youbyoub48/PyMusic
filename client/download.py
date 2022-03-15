import requests, urllib.request, vlc, time

def Download(pseudo):
    r = requests.get(f"http://51.91.251.170/api/get/pseudo={pseudo}")
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


if __name__ == "__main__":
    Download(pseudo="test")