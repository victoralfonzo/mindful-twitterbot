import tweepy
import schedule
import time

def gatherQuote():
    print("quote gathered")
    line = None
    with open("current.txt","r+") as progress:
        current = int(progress.read())
        with open("quotes.txt") as f:
            line = f.read().split("\n")[current]
            print(line)
        try:
            api.update_status(line)
        except tweepy.TweepError as e:
            print(e.reason)
        progress.seek(0)
        progress.write(str(current+2))
        progress.close()

auth = tweepy.OAuthHandler(consumer_token, consumer_secret)
auth.set_access_token(key, secret)

api = tweepy.API(auth)

schedule.every().day.at("00:00:00").do(gatherQuote)
schedule.every().day.at("12:00:00").do(gatherQuote)

while True:
    schedule.run_pending()
    time.sleep(1)
