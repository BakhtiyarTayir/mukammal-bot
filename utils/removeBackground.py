import requests
import logging


import requests

url = "https://background-removal.p.rapidapi.com/remove"

headers = {
	"content-type": "application/x-www-form-urlencoded",
	"X-RapidAPI-Host": "background-removal.p.rapidapi.com",
	"X-RapidAPI-Key": "215aa0eb03msh10df8028da554e5p13c2e2jsne414b3e1a257"
}




async def remove_background(image_url):
    payload = f"image_url={image_url}"
    response = requests.request("POST", url, data=payload, headers=headers)
    logging.info(response.json().keys())
    return response.json()['response']['image_url']


if __name__ == "__main__":

    print(remove_background("https://telegra.ph//file/0df6e4f5ca29f80745207.jpg"))