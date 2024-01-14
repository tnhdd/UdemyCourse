import requests

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything?"

STOCK_API_KEY = "PMVUWB60PCNX1UIP"
NEWS_API_KEY = "883780ed19f84e3a97b106aebcdbb35b"

# STEP 1: Use https://www.alphavantage.co
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").
stock_param = {
    "function": "TIME_SERIES_DAILY_ADJUSTED",
    "symbol": STOCK,
    "apikey": STOCK_API_KEY
}
response = requests.get(STOCK_ENDPOINT, params=stock_param)
data = response.json()["Time Series (Daily)"]
data_list = [value for (key,value) in data.items()]

yesterday_data = data_list[0]
yesterday_closing_price = yesterday_data["4. close"]

day_before_yesterday = data_list[1]
day_before_yesterday_closing_price = day_before_yesterday["4. close"]

price_different = float(yesterday_closing_price) - float(day_before_yesterday_closing_price)
price_different = round(price_different,2)

print(f"Yesterday closing price: {yesterday_closing_price}")
print(f"Day before yesterday closing price: {day_before_yesterday_closing_price}")

if price_different > 0 :
    percentage = round((price_different / float(yesterday_closing_price)) * 100,2)
    print(f"Price increse: {percentage}%")
elif price_different < 0:
    percentage =round ((-price_different / float(yesterday_closing_price)) * 100,2)
    print(f"Price decrease: {percentage}%")



# STEP 2: Use https://newsapi.org
# Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME.
news_params = {
    "q":"Tesla",
    "apiKey": NEWS_API_KEY
}
response_news = requests.get(NEWS_ENDPOINT, params=news_params)

data_news = response_news.json()
articles = response_news.json()["articles"]
three_articles = articles[:3]
print(three_articles)

# STEP 3: Use https://www.twilio.com
# Send a separate message with the percentage change and each article's title and description to your phone number.


# Optional: Format the SMS message like this:
"""
TSLA: 🔺2% Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. Brief: We at Insider Monkey have 
gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings 
show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash. 
or 
"TSLA: 🔻5% Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. Brief: We at Insider Monkey 
have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F 
filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus 
market crash.
"""
