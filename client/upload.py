import requests

def Upload(pseudo, lien):
    requests.post(f"http://51.91.251.170/api/post/pseudo={pseudo}", data={"lien": lien})


if __name__ == "__main__":
    pseudo = "test"
    lien = "https://www.youtube.com/watch?v=LDU_Txk06tM"
    Upload(pseudo, lien)