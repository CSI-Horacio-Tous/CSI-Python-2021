import requests
import bs4

webpage = requests.get("https://forecast.weather.gov/MapClick.php?lat=18.466330000000028&lon=-66.10472999999996#.YkroRZnMJPY")
soup = bs4.BeautifulSoup(webpage.content, "html.parser")
sevenDay = soup.find(id="seven-day-forecast")
forecast_item = sevenDay.find_all(class_="tombstone-container")
tonight = forecast_item[1]

period = tonight.find(class_="period-name").get_text()
print(period)
short = tonight.find(class_="short-desc").get_text()
temp = tonight.find(class_="temp temp-low").get_text()
print(short)
print(temp)
