# Mindfulness Twitter Bot
Twitter bot that tweets mindfulness quotes sourced from [Goodreads](https://www.goodreads.com/quotes/tag/mindfulness)

## Dependencies
- Beautiful Soup 
- Tweepy 


## Bot Setup

Simply install the dependencies using `pip`

```
pip install beautifulsoup4
pip install tweepy
```

Next, [register an application with twitter](https://developer.twitter.com/) to receive the necessary authentification keys to set up the bot. 

You will need 
- Consumer Key (API Key)
- Consumer Secret (API Secret)
- Access Token
- Access Token Secret

In bot.py, replace `consumer_token`, `consumer_secret`, `key`, and `secret`, with your application's respective keys.

```
auth = tweepy.OAuthHandler(consumer_token, consumer_secret)
auth.set_access_token(key, secret)
```
For more information about the authentification process, refer to [tweepy's tutorial](http://docs.tweepy.org/en/v3.5.0/auth_tutorial.html).

## Quote Scraping

To scrape the quotes from [Goodreads](https://www.goodreads.com/quotes/tag/mindfulness), simply run

```
python quoteScraper.py
```
in the project directory.

This will append all quotes from `page` of Goodread's mindfulness quotes to quotes.txt, removing all unnecessary characters.

## Usage

To start the bot, simply run 

```
python bot.py
```
in the project directory.
