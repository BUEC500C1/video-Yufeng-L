# Get tweets and then insert into images
import os
import tweepy
import re
from PIL import Image, ImageDraw, ImageFont

# insert your key
consumer_key = ''
consumer_secret = ''
access_token = ''
access_token_secret = ''
  
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)  
auth.set_access_token(access_token, access_token_secret)   
api = tweepy.API(auth)
search_results = api.user_timeline('BU_Tweets') # Default Count = 20
image = Image.open('background.png') # Background Image for insert
count = 0
Ignore = re.compile(u'[\uD800-\uDBFF][\uDC00-\uDFFF]')
print("Start Inserting")
for tweet in search_results:
	gap = '\n'
	tweet_list = list(tweet.text)
	list_num = 0
	for i in range(len(tweet_list)):
		if (i % 50) == 0:
			tweet_list.insert(i,gap)
	tweet.text = ''.join(tweet_list)

	count += 1

	fnt = ImageFont.truetype('/Library/Fonts/Arial.ttf', 50)
	draw = ImageDraw.Draw(image)
	draw.text((100,200), tweet.text, font=fnt, fill= "black")
	filename = "tweets/img" + str(count) + ".png"
	image.save(filename)

print("Insert Completed")






