import requests

url = "https://api.yelp.com/v3/businesses/search"
api_key = "*****"

headers = {
	"Authorization":"Bearer " + api_key
}

params = {
	"term" :"Sushi",
	"location":"winnipeg"
}

response  = requests.get(url, headers=headers, params=params)

businesses= response.json()["businesses"]
print (businesses)

names = [businesse["name"] for businesse in businesses if businesse["rating"]>4.5]
print (names)
