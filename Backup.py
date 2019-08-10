from textblob import TextBlob
import sys, tweepy
import matplotlib.pyplot as plt
def percentage(part,whole):
    return 100*float(part)/float(whole)
consumer_key = 'dgF6sCPtaVDRUWot9TbSgf2LY'
consumer_secret = 'XtdRBJKMtzBNUVgsqhSslANHnrg6l6zY8ym2JdCwA42bqmNHNX'
access_token = '593708055-Yct2sEizAPdBicQXstyfy4L1Clm9xFEJ3x9KNFOz'
access_secret = 'ItP5OdEaCT9LeCXNpIXCX5nNoH9I1gD9jSPdQL7VcUXvt'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)
api = tweepy.API(auth)

searchTerm = input("Enter keyword/hashtag to search about: ")
noOfSearchTerms= int(input("Enter how many tweets to analyze: "))

tweets = tweepy.Cursor(api.search, q = searchTerm ,result_type="recent", lang="en").items(noOfSearchTerms)

positive = 0
negative = 0
neutral = 0
polarity = 0
for tweet in tweets:
    # print(tweet.text)
    analysis = TextBlob(tweet.text)
    polarity+=analysis.sentiment.polarity
    # print(analysis.sentiment.polarity)
    if (analysis.sentiment.polarity == 0):
        neutral+=1
    elif (analysis.sentiment.polarity < 0.00):
        negative+=1
    elif (analysis.sentiment.polarity > 0.00):
        positive+=1
positive = percentage(positive, noOfSearchTerms)
negative = percentage(negative, noOfSearchTerms)
neutral = percentage(neutral, noOfSearchTerms)
polarity = percentage(polarity, noOfSearchTerms)
# print("Positive = ",positive)
# print("Negative = ",negative)
# print("Neutral = ",neutral)

positive = format(positive,'.2f')
negative = format(negative,'.2f')
neutral = format(neutral,'.2f')


labels = ['Positive ['+str(positive)+'%]', 'Neutral ['+str(neutral)+'%]', 'Negative ['+str(negative)+'%]']

sizes = [positive,neutral, negative]
colors = ['yellowgreen','gold','red']
patches,texts = plt.pie(sizes, colors = colors, startangle = 90)
plt.legend(patches, labels, loc = "best")
plt.title('How people are reacting on '+searchTerm+' by analyzing '+str(noOfSearchTerms)+' Tweets. ')
plt.axis('equal')
plt.tight_layout()
plt.show()
# if(polarity == 0):
#     print("neutral")
# elif(polarity < 0):
#     print("negative")
# elif(polarity > 0):
#     print("positive")