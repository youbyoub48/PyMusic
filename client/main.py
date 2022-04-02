from download import Download
from friends import add_friends
from upload import Upload

ip = "127.0.0.1:8000"
pseudo = input("quel est-votre pseudo:")
mode = int(input("quel mode ? 1-2:"))

if mode == 1:
    Download(ip, pseudo)

elif mode == 2:
    amis = input("pseudo de votre amis ?:")
    add_friends(ip ,pseudo, amis)
    lien = input("lien de votre musique youtube:")
    Upload(ip, pseudo, lien)