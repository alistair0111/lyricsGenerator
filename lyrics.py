import configparser
import requests


def getAccessToken():
    config = configparser.ConfigParser()
    config.read('config.ini')
    return config['Client_Access_Token']['token']


token = getAccessToken()


def searchMusicArtist(name):
    api_url = "https://api.genius.com/search?q={}".format(name)
    headers = {"authorization": token}
    r = requests.get(api_url, headers=headers)
