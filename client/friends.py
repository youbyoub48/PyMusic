import requests

def add_friends(ip, pseudo, pseudo2):
    requests.get(f"http://{ip}/api/get/ajout/pseudo={pseudo}&pseudo2={pseudo2}")

def get_friends():pass

# sourcery skip: use-itertools-product
if __name__ == "__main__":
    from time import sleep

    ip = "127.0.0.1:8000"
    for i in range(4):
        for x in range(4):
            add_Friend(ip ,f"test{i}", f"amis{x}")
            sleep(1)