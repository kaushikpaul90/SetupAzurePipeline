import requests

url = "https://exercisedb.p.rapidapi.com/exercises/bodyPart/chest"

querystring = {"limit":"10"}

headers = {
	"X-RapidAPI-Key": "7a17ecd123msh1aa9a12e1ce81abp150bc3jsn4057487891a0",
	"X-RapidAPI-Host": "exercisedb.p.rapidapi.com"
}

response = requests.get(url, headers=headers, params=querystring)

print(response.json())