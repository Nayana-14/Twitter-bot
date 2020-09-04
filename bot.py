import tweepy
import time

consumer_key = 'viiUq78cJKvueocKSwrXtnA31'
consumer_secret = 'huZUzbBwN59AwTqomqh7MeHRNB0JygYf03TywTM1sCdNgZxAMA'
key = '1117661466729910272-61LP2vgzqrKJQTD2nGxRiSbRCHskXs'
secret = '5dljJxR2ehKhDrnKdA6NZDqZcq2TAT2N3OXTpMFcp7duU'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(key, secret)

api = tweepy.API(auth)
#api.update_status('Hello by my first twitter bot!')
#print('Status Updated')


# print(tweets)
# print(tweets[1])
# print(tweets[1].id)


FILE_NAME = 'seen.txt'


def read_seen(FILE_NAME):
    file_read = open(FILE_NAME, 'r')
    record_id = int(file_read.read().strip())
    file_read.close()
    return record_id

#id = read_seen(FILE_NAME)
# print(id)

# reading the tweet id's


def store_seen(FILE_NAME, record_id):
    file_write = open(FILE_NAME, 'w')
    file_write.write(str(record_id))
    file_write.close()
    return


def reply_tweet():
    tweets = api.mentions_timeline(read_seen(FILE_NAME), tweet_mode='extended')
    for tweet in reversed(tweets):
        if '#anything' in tweet.full_text.lower():
            #print("New Tweet Found!")
            print(str(tweet.id) + ' - ' + tweet.full_text)

            api.update_status("@" + tweet.user.screen_name +
                              " Thanks for tweeting, Have a nice day! #anything", tweet.id)

            store_seen(FILE_NAME, tweet.id)


while True:
    # this will remain true forever
    reply_tweet()
    time.sleep(30)
