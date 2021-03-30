import os
import requests
import random
from twilio.rest import Client
from twilio.http.http_client import TwilioHttpClient

STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"

api_key = 'bba0165d8b80526c1e16ef603496d2b6'
account_sid = 'AC4c313d5ccb4c34b9b0f167e9a02fba24'
auth_token = 'af1b725a1eade63a9f341db71e78f83a'

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

STOCK_PARAMETERS = {
    'apikey': 'VL55H8KD99VC790D',
    'function': 'TIME_SERIES_DAILY',
    'symbol': STOCK_NAME
}

NEWS_PARAMETERS = {
    'apiKey': 'bece93cf2e9d47b6b53ef6bc7dab7b02',
    'q': COMPANY_NAME
}

response = requests.get(STOCK_ENDPOINT, params=STOCK_PARAMETERS)

days = response.json()['Time Series (Daily)']
lst = []

for day in days:
    lst.append(day)

day1 = float(days[lst[0]]['4. close'])
day2 = float(days[lst[1]]['4. close'])

arrow = '🔺' if day1-day2 > 0 else '🔻'
percent = str(abs(day1 - day2) / day2 * 100).split('.')[0]

if int(percent) > 0:
    response = requests.get(NEWS_ENDPOINT, params=NEWS_PARAMETERS)
    articles = response.json()['articles']
    three_articles = [(articles[i]['title'], articles[i]['description']) for i in range(3)]

    proxy_client = TwilioHttpClient()
    proxy_client.session.proxies = {'https': os.environ['https_proxy']}
    client = Client(account_sid, auth_token, http_client=proxy_client)
    num = random.randint(0, 2)
    message = client.messages \
        .create(
        body=f"{STOCK_NAME}: {arrow}{percent}%\nHeadline: {three_articles[num][0]}\nBrief: {three_articles[num][1]}",
        from_='+14159961359',
        to='+19292549035'
    )
    print(message.status)
    
# When stock price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").

#TODO 1. - Get yesterday's closing stock price. Hint: You can perform list comprehensions on Python dictionaries. e.g. [new_value for (key, value) in dictionary.items()]

#TODO 2. - Get the day before yesterday's closing stock price

#TODO 3. - Find the positive difference between 1 and 2. e.g. 40 - 20 = -20, but the positive difference is 20. Hint: https://www.w3schools.com/python/ref_func_abs.asp

#TODO 4. - Work out the percentage difference in price between closing price yesterday and closing price the day before yesterday.

#TODO 5. - If TODO4 percentage is greater than 5 then print("Get News").

    ## STEP 2: https://newsapi.org/ 
    # Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME. 

#TODO 6. - Instead of printing ("Get News"), use the News API to get articles related to the COMPANY_NAME.

#TODO 7. - Use Python slice operator to create a list that contains the first 3 articles. Hint: https://stackoverflow.com/questions/509211/understanding-slice-notation


    ## STEP 3: Use twilio.com/docs/sms/quickstart/python
    #to send a separate message with each article's title and description to your phone number. 

#TODO 8. - Create a new list of the first 3 article's headline and description using list comprehension.

#TODO 9. - Send each article as a separate message via Twilio.

#Optional TODO: Format the message like this: 
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""

