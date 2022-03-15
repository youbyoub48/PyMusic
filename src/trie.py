import os, shutil, json
from glob import glob

def Trie(pseudo):
    PATH =os.path.abspath(os.path.split(__file__)[0])
    fichier = glob(os.path.join(PATH, "*.mp3"))
    print(fichier)
    musique = fichier[0].replace(PATH,"")
    musique = musique.replace(".mp3","")
    musique = musique.replace("/","")
    #musique = musique.replace(" ","_")
    print(musique)

    with open("musique.json", "w") as f:
        save = {pseudo: musique}
        json.dump(save, f)

    #os.rename(fichier[0], os.path.join(PATH, f"{musique}.mp3"))
    shutil.copy(fichier[0], "/var/www/html")
    os.remove(fichier[0])

if __name__ == "__main__":
    Trie("test")