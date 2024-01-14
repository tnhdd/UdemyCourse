from bs4 import BeautifulSoup
import requests

response = requests.get("https://news.ycombinator.com/")
yc_web_page = response.text

soup = BeautifulSoup(yc_web_page, "html.parser")
articles = soup.find(name="a", class_="storylink")
articles_texts = []
articles_links = []
for article_tag in articles:
    article_text = article_tag.getTex()
    article_link = article_tag.get("href")
article_upvotes = soup.find_all(name="span", class_="score").getText()
print(article_upvotes)

print(article_text)
