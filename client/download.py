import requests, urllib.request, vlc, time

def Download(pseudo):
    r = requests.get(f"http://51.91.251.170/api/get/pseudo={pseudo}")
    print(r.status_code)
    dico = r.json()

    for element in dico:
        musique = element
        lien = str(dico[musique])
        lien = lien.replace(" ","%20")
        lien = lien.replace("[","%5b")
        lien = lien.replace("]","%5d")
        print(lien)
        urllib.request.urlretrieve(lien, f"{musique}.mp3")
        time.sleep(2)

    p = vlc.MediaPlayer(f"{musique}.mp3")
    p.play()
    time.sleep(0.5)
    Millisecondes = p.get_length()
    Secondes = Millisecondes*0.001
    print(Secondes)
    time.sleep(Secondes)


if __name__ == "__main__":
    Download(pseudo="youbyoub2")