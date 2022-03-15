from download import Download
from ajout import Ajout
from upload import Upload

pseudo = input("quel est-votre pseudo")
mode = int(input("quel mode ? 1-2:"))

if mode == 1:
    Download(pseudo)

elif mode == 2:
    amis = input("pseudo de votre amis ?:")
    Ajout(pseudo, amis)
    lien = input("lien de votre musique youtube:")
    Upload(pseudo, lien)