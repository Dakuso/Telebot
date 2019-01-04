import json
import requests

url = "https://api.scryfall.com"
cards = url + "/cards"

data = requests.get(cards).json()

i = 0

def Create_dict():
    Card_dict = {}

    while data["has_more"]:

        for element in data["data"]:                    #write keys in Card list
            name = element["name"]
            Card_dict["name"] = element

        if not data["has_more"] == false:               #Turn Page
            data = requests.get(cards["next_page"])


        else:
            with open("DATA", "w") as fo:
                json.dump(Card_dict, fo)
            break


def card_request():
    Card_dict = json.load(open("DATA"))
    while true:
        cardname = input("Enter your cardname")

        if "cardname" in Card_dict.keys():          #zugriff auf img
            print(Card_dict["cardname"]["image_uris"]["png"])
            break
        else:
            print("did you mean Terminus ?")
            print(Card_dict["Terminus"]["image_uris"]["png"])



