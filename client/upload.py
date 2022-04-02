import requests

def Upload(ip, pseudo, lien):
    requests.post(f"http://{ip}/api/post/pseudo={pseudo}", data={"lien": lien})


if __name__ == "__main__":
    ip = "127.0.0.1:8000"
    pseudo = "test"
    lien = "https://www.youtube.com/watch?v=LDU_Txk06tM"
    Upload(ip, pseudo, lien)