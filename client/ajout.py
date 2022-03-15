import requests

def Ajout(pseudo, pseudo2):
    requests.get(f"api/get/ajout/pseudo={pseudo}&pseudo2={pseudo2}")
