import requests

url_w = "https://weather.com/weather/today/l/94560"
url = "https://www.weather.com"

def joke():
	url = "https://icanhazdadjoke.com/search"
	q_string = input("Input category of joke : ")
	res = requests.get(
					url, 
					headers={"Accept": "application/json"}, 
					params= {"term":q_string})

	joke_data = res.json()
	print(joke_data)
	joke_len = len(joke_data['results'])

	print(f"I've got {str(joke_len)} jokes about '{q_string}'")
	for i in range(joke_len):
		print(f"{i+1}) " + joke_data['results'][i]['joke'])

def weather():
	url_w = "https://weather.com/weather/today/l/94560"
	
	res = requests.get(url_w,
							headers={"Accept":"text/html"},
							)
	#weather_data = res.json()
	print(res.text)

if __name__ == "__main__":
	weather()