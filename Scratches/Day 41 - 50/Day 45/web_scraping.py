import requests
from bs4 import BeautifulSoup

url = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

response = requests.get(url)
yc_web = response.text
soup = BeautifulSoup(yc_web, "html.parser")
movies = soup.find_all(name="h3", class_="title")
list_movies = []
for movie in movies:
    list_movies.append(movie.text)
list_movies.reverse()
with open("list.txt", "w", encoding="utf-8") as file:
    for item in list_movies:
        file.write(str(item) + "\n")
