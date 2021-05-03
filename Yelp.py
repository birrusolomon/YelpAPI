import requests

url = "https://api.yelp.com/v3/businesses/search"
api_key = "pjbND36fWbaNW46xKYznbGWdeRmMYeu8ZVCg-5rcr54qXQSy0qg_X0jSS8ltCmQvKdJyxxb0iZJPlsbvaNE5lkGGxVdc1EYAgeAheXVx5hheAmV2tLZubbq0Orj8X3Yx"

headers = {
	"Authorization":"Bearer " + api_key
}

params = {
	"term" :"ethiopian",
	"location":"winnipeg"
}

response  = requests.get(url, headers=headers, params=params)

businesses= response.json()["businesses"]
print (businesses)

names = [businesse["name"] for businesse in businesses if businesse["rating"]>4.5]
print (names)
